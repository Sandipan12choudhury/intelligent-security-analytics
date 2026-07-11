"""
==============================================================================
Report Service

Purpose
-------
Builds PDF security reports at three scopes - Application, Department,
and Enterprise-wide - using the existing analytics datasets (no
scoring logic is reimplemented here, only formatting).

Every generated report is saved under /reports and logged to
reports_log.json, so the Reports page can show a re-downloadable
history in addition to generating new ones.

Author
------
Sandipan Choudhury
==============================================================================
"""

import io
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable
)

from backend.dataset_manager import dataset_manager
from backend.services.observation_service import ObservationService
from backend.logging_config import data_logger

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

REPORTS_DIR = PROJECT_ROOT / "reports"

REPORTS_LOG_PATH = REPORTS_DIR / "reports_log.json"

REPORTS_DIR.mkdir(exist_ok=True)

# =============================================================================
# Brand Palette
# =============================================================================

NAVY = colors.HexColor("#0f172a")

SLATE = colors.HexColor("#334155")

MUTED = colors.HexColor("#64748b")

FAINT = colors.HexColor("#94a3b8")

ACCENT = colors.HexColor("#2563eb")

LINE = colors.HexColor("#e2e8f0")

CARD_BG = colors.HexColor("#f8fafc")

ZEBRA = colors.HexColor("#f8fafc")

HIGH_RED = colors.HexColor("#dc2626")

MEDIUM_AMBER = colors.HexColor("#d97706")

LOW_GREEN = colors.HexColor("#16a34a")

STYLES = getSampleStyleSheet()

TITLE_STYLE = ParagraphStyle(

    "TitleStyle",
    parent=STYLES["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=19,
    textColor=colors.white,
    spaceAfter=2

)

SUBTITLE_BAND_STYLE = ParagraphStyle(

    "SubtitleBandStyle",
    parent=STYLES["Normal"],
    fontName="Helvetica",
    fontSize=10.5,
    textColor=colors.HexColor("#c7d2fe"),

)

SUBTITLE_STYLE = ParagraphStyle(

    "SubtitleStyle",
    parent=STYLES["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=15,
    textColor=NAVY,
    spaceBefore=22,
    spaceAfter=10

)

HEADING_STYLE = ParagraphStyle(

    "HeadingStyle",
    parent=STYLES["Heading3"],
    fontName="Helvetica-Bold",
    fontSize=12,
    textColor=NAVY,
    spaceBefore=20,
    spaceAfter=4

)

BODY_STYLE = ParagraphStyle(

    "BodyStyle",
    parent=STYLES["BodyText"],
    fontName="Helvetica",
    fontSize=9.5,
    leading=14,
    textColor=SLATE

)

CARD_VALUE_STYLE = ParagraphStyle(

    "CardValueStyle",
    parent=STYLES["Normal"],
    fontName="Helvetica-Bold",
    fontSize=16,
    textColor=NAVY,
    leading=19

)

CARD_LABEL_STYLE = ParagraphStyle(

    "CardLabelStyle",
    parent=STYLES["Normal"],
    fontName="Helvetica",
    fontSize=7.6,
    textColor=MUTED,
    leading=10

)

OBS_HEADING_STYLE = ParagraphStyle(

    "ObsHeading",
    parent=BODY_STYLE,
    fontName="Helvetica-Bold",
    textColor=NAVY,
    fontSize=9.5,
    spaceBefore=11,
    spaceAfter=2

)


def _rule():

    return HRFlowable(

        width="100%",
        thickness=0.75,
        color=LINE,
        spaceBefore=2,
        spaceAfter=12

    )


def _severity_color(level):

    level = (level or "").lower()

    if level == "high":

        return HIGH_RED

    if level == "medium":

        return MEDIUM_AMBER

    if level == "low":

        return LOW_GREEN

    return MUTED


SEVERITY_HEX = {

    "high": "#dc2626",
    "medium": "#d97706",
    "low": "#16a34a"

}


def _severity_hex(level):

    return SEVERITY_HEX.get((level or "").lower(), "#64748b")


def _kpi_grid(pairs, columns=3):

    """
    Renders KPI values as a grid of bordered "cards" (big bold value,
    small muted caption underneath) instead of a plain label:value
    table.
    """

    card_width = 16.4 / columns

    rows = []

    current_row = []

    for label, value in pairs:

        cell = Table(

            [[
                Paragraph(str(value), CARD_VALUE_STYLE)
            ], [
                Paragraph(label.upper(), CARD_LABEL_STYLE)
            ]],

            colWidths=[card_width * cm - 0.3 * cm]

        )

        cell.setStyle(TableStyle([

            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),

        ]))

        current_row.append(cell)

        if len(current_row) == columns:

            rows.append(current_row)

            current_row = []

    if current_row:

        while len(current_row) < columns:

            current_row.append("")

        rows.append(current_row)

    grid = Table(

        rows,

        colWidths=[card_width * cm] * columns,

        rowHeights=[1.55 * cm] * len(rows)

    )

    style_commands = [

        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),

    ]

    for r in range(len(rows)):

        for c in range(columns):

            style_commands.append(

                ("BOX", (c, r), (c, r), 0.75, LINE)

            )

            style_commands.append(

                ("BACKGROUND", (c, r), (c, r), CARD_BG)

            )

    grid.setStyle(TableStyle(style_commands))

    return grid


def _data_table(header, rows, col_widths, severity_col=None):

    table_data = [header] + rows

    table = Table(table_data, colWidths=col_widths, repeatRows=1)

    style_commands = [

        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("TEXTCOLOR", (0, 1), (-1, -1), SLATE),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE),

    ]

    for i in range(1, len(table_data)):

        if i % 2 == 0:

            style_commands.append(

                ("BACKGROUND", (0, i), (-1, i), ZEBRA)

            )

    if severity_col is not None:

        for i, row in enumerate(rows, start=1):

            style_commands.append((

                "TEXTCOLOR",
                (severity_col, i),
                (severity_col, i),
                _severity_color(row[severity_col])

            ))

            style_commands.append((

                "FONTNAME",
                (severity_col, i),
                (severity_col, i),
                "Helvetica-Bold"

            ))

    table.setStyle(TableStyle(style_commands))

    return table


def _page_decoration(canvas, doc):

    canvas.saveState()

    page_width, page_height = A4

    # Top navy band

    canvas.setFillColor(NAVY)

    canvas.rect(0, page_height - 2.6 * cm, page_width, 2.6 * cm, fill=1, stroke=0)

    canvas.setFillColor(ACCENT)

    canvas.rect(0, page_height - 2.65 * cm, page_width, 0.06 * cm, fill=1, stroke=0)

    canvas.setFillColor(colors.white)

    canvas.setFont("Helvetica-Bold", 13)

    canvas.drawString(

        1.8 * cm, page_height - 1.5 * cm,

        "Intelligent Security Analytics Platform"

    )

    canvas.setFont("Helvetica", 8.5)

    canvas.setFillColor(colors.HexColor("#c7d2fe"))

    canvas.drawString(

        1.8 * cm, page_height - 2.05 * cm,

        "Enterprise Security Assessment & Risk Intelligence"

    )

    # Footer

    canvas.setStrokeColor(LINE)

    canvas.line(1.8 * cm, 1.35 * cm, page_width - 1.8 * cm, 1.35 * cm)

    canvas.setFont("Helvetica", 7.5)

    canvas.setFillColor(FAINT)

    canvas.drawString(

        1.8 * cm, 0.9 * cm,

        f"Generated {datetime.now(timezone.utc).strftime('%d %b %Y, %H:%M')} "
        f"| Intelligent Security Analytics Platform - Confidential"

    )

    canvas.drawRightString(

        page_width - 1.8 * cm, 0.9 * cm,

        f"Page {canvas.getPageNumber()}"

    )

    canvas.restoreState()


class ReportNotFoundError(Exception):

    pass


class ReportService:

    def __init__(self):

        self.observation_service = ObservationService()

    # ============================================================
    # Application Report
    # ============================================================

    def _build_application_report(self, application_id: str):

        app_analytics_df = dataset_manager.get_application_analytics()

        app_row = app_analytics_df[

            app_analytics_df["Application ID"] == application_id

        ]

        if app_row.empty:

            raise ReportNotFoundError(

                f"Application {application_id} was not found."

            )

        app = app_row.iloc[0]

        observations = self.observation_service.get_observations()[

            "observations"

        ]

        app_observations = [

            obs for obs in observations

            if obs.get("Application ID") == application_id

        ]

        elements = []

        elements.append(

            Paragraph(

                f"Application Security Report",

                SUBTITLE_STYLE

            )

        )

        elements.append(

            Paragraph(

                f"<b>{app['Application ID']}</b> &nbsp;-&nbsp; "
                f"{app['Application Name']} &nbsp;|&nbsp; "
                f"{app['Department']}",

                BODY_STYLE

            )

        )

        elements.append(_rule())

        elements.append(_kpi_grid([

            ("Risk Score", f"{app['Risk Score']} / 100"),
            ("Risk Category", app["Risk Category"]),
            ("Executive Priority", app["Executive Priority"]),
            ("Compliance %", f"{app['Compliance %']}%"),
            ("Compliance Grade", app["Compliance Grade"]),
            ("Total Observations", int(app["Total Observations"])),

        ]))

        elements.append(Paragraph("Severity Distribution", HEADING_STYLE))

        elements.append(_data_table(

            ["Severity", "Count", "%"],

            [
                ["High", int(app["High Count"]), f"{app['High %']}%"],
                ["Medium", int(app["Medium Count"]), f"{app['Medium %']}%"],
                ["Low", int(app["Low Count"]), f"{app['Low %']}%"],
            ],

            [5.4 * cm, 5.5 * cm, 5.5 * cm],

            severity_col=0

        ))

        elements.append(Paragraph("Activity Breakdown", HEADING_STYLE))

        elements.append(_data_table(

            ["Activity", "Count", "%"],

            [
                ["ITGC", int(app["ITGC Count"]), f"{app['ITGC %']}%"],
                ["Database", int(app["Database Count"]), f"{app['Database %']}%"],
                ["DFRA", int(app["DFRA Count"]), f"{app['DFRA %']}%"],
                ["DFA / DFD", int(app["DFA Count"]), f"{app['DFA %']}%"],
                ["SNA", int(app["SNA Count"]), f"{app['SNA %']}%"],
            ],

            [5.4 * cm, 5.5 * cm, 5.5 * cm]

        ))

        elements.append(PageBreak())

        elements.append(

            Paragraph(

                f"All Observations ({len(app_observations)})",

                SUBTITLE_STYLE

            )

        )

        elements.append(_rule())

        for obs in app_observations:

            elements.append(

                Paragraph(

                    f"<font color='#0f172a'>{obs['Observation ID']}</font>"
                    f" &nbsp; "
                    f"<font color='{_severity_hex(obs['Severity'])}'>"
                    f"[{obs['Severity']}]</font>"
                    f" &nbsp; "
                    f"<font color='#64748b'>{obs['Activity']} - {obs['Domain']}</font>",

                    OBS_HEADING_STYLE

                )

            )

            elements.append(Paragraph(obs["Observation"], BODY_STYLE))

        elements.append(Spacer(1, 10))

        title = f"{app['Application ID']}_{app['Application Name']}"

        return elements, f"Application Report - {app['Application Name']}", title

    # ============================================================
    # Department Report
    # ============================================================

    def _build_department_report(self, department: str):

        dept_analytics_df = dataset_manager.get_department_analytics()

        dept_row = dept_analytics_df[

            dept_analytics_df["Department"] == department

        ]

        if dept_row.empty:

            raise ReportNotFoundError(

                f"Department '{department}' was not found."

            )

        dept = dept_row.iloc[0]

        app_analytics_df = dataset_manager.get_application_analytics()

        dept_apps = app_analytics_df[

            app_analytics_df["Department"] == department

        ].sort_values("Risk Score", ascending=False)

        elements = []

        elements.append(

            Paragraph("Department Security Report", SUBTITLE_STYLE)

        )

        elements.append(

            Paragraph(f"<b>{department}</b>", BODY_STYLE)

        )

        elements.append(_rule())

        elements.append(_kpi_grid([

            ("Applications", int(dept["Applications"])),
            ("Total Observations", int(dept["Total Observations"])),
            ("Average Risk Score", f"{dept['Average Risk Score']} / 100"),
            ("Risk Category", dept["Risk Category"]),
            ("Executive Priority", dept["Executive Priority"]),
            ("Average Compliance %", f"{dept['Average Compliance %']}%"),
            ("Compliance Grade", dept["Compliance Grade"]),
            ("Top Activity", f"{dept['Top Activity']} ({dept['Top Activity %']}%)"),
            ("Highest Risk App", dept["Highest Risk Application Name"]),

        ]))

        elements.append(Paragraph("Severity Distribution", HEADING_STYLE))

        elements.append(_data_table(

            ["Severity", "Count", "%"],

            [
                ["High", int(dept["High Count"]), f"{dept['High %']}%"],
                ["Medium", int(dept["Medium Count"]), f"{dept['Medium %']}%"],
                ["Low", int(dept["Low Count"]), f"{dept['Low %']}%"],
            ],

            [5.4 * cm, 5.5 * cm, 5.5 * cm],

            severity_col=0

        ))

        elements.append(

            Paragraph(

                f"Applications in this Department ({len(dept_apps)})",

                HEADING_STYLE

            )

        )

        app_rows = [

            [
                row["Application ID"],
                row["Application Name"],
                f"{row['Risk Score']}",
                row["Risk Category"],
                int(row["Total Observations"])
            ]

            for _, row in dept_apps.iterrows()

        ]

        elements.append(_data_table(

            ["ID", "Application", "Risk Score", "Category", "Observations"],

            app_rows,

            [2.3 * cm, 5.7 * cm, 2.7 * cm, 2.7 * cm, 2.6 * cm]

        ))

        elements.append(Spacer(1, 10))

        return elements, f"Department Report - {department}", department

    # ============================================================
    # Enterprise Report
    # ============================================================

    def _build_enterprise_report(self):

        enterprise = dataset_manager.get_enterprise_analytics().iloc[0]

        dept_df = dataset_manager.get_department_analytics().sort_values(

            "Department Rank"

        )

        activity_df = dataset_manager.get_activity_analytics().sort_values(

            "Enterprise Rank"

        )

        elements = []

        elements.append(

            Paragraph("Enterprise-Wide Security Report", SUBTITLE_STYLE)

        )

        elements.append(

            Paragraph(f"<b>{enterprise['Enterprise Name']}</b>", BODY_STYLE)

        )

        elements.append(_rule())

        elements.append(_kpi_grid([

            ("Departments", int(enterprise["Departments"])),
            ("Applications", int(enterprise["Applications"])),
            ("Total Observations", int(enterprise["Total Observations"])),
            ("Average Risk Score", f"{enterprise['Average Risk Score']} / 100"),
            ("Risk Category", enterprise["Risk Category"]),
            ("Executive Priority", enterprise["Executive Priority"]),
            ("Average Compliance %", f"{enterprise['Average Compliance %']}%"),
            ("Compliance Grade", enterprise["Compliance Grade"]),
            ("Highest Risk Dept.", enterprise["Highest Risk Department"]),

        ]))

        elements.append(Paragraph("Department Comparison", HEADING_STYLE))

        dept_rows = [

            [
                row["Department"],
                f"{row['Average Risk Score']}",
                row["Risk Category"],
                f"{row['Average Compliance %']}%",
                int(row["Total Observations"])
            ]

            for _, row in dept_df.iterrows()

        ]

        elements.append(_data_table(

            ["Department", "Risk Score", "Category", "Compliance", "Observations"],

            dept_rows,

            [5 * cm, 2.5 * cm, 2.5 * cm, 2.5 * cm, 3 * cm]

        ))

        elements.append(Paragraph("Activity Summary", HEADING_STYLE))

        activity_rows = [

            [
                row["Activity"],
                f"{row['Risk Score']}",
                row["Risk Category"],
                int(row["Total Observations"])
            ]

            for _, row in activity_df.iterrows()

        ]

        elements.append(_data_table(

            ["Activity", "Risk Score", "Category", "Observations"],

            activity_rows,

            [5 * cm, 3 * cm, 3 * cm, 4 * cm]

        ))

        elements.append(Spacer(1, 10))

        return elements, "Enterprise-Wide Report", "Enterprise"

    # ============================================================
    # Public entry point
    # ============================================================

    def generate_report(self, report_type: str, scope: str = None):

        if report_type == "application":

            elements, label, scope_name = self._build_application_report(scope)

        elif report_type == "department":

            elements, label, scope_name = self._build_department_report(scope)

        elif report_type == "enterprise":

            elements, label, scope_name = self._build_enterprise_report()

        else:

            raise ValueError(

                "report_type must be 'application', 'department', "
                "or 'enterprise'."

            )

        buffer = io.BytesIO()

        doc = SimpleDocTemplate(

            buffer,

            pagesize=A4,

            topMargin=3.3 * cm,

            bottomMargin=2 * cm,

            leftMargin=1.8 * cm,

            rightMargin=1.8 * cm

        )

        doc.build(

            elements,

            onFirstPage=_page_decoration,

            onLaterPages=_page_decoration

        )

        pdf_bytes = buffer.getvalue()

        report_id = str(uuid.uuid4())[:8]

        safe_scope = "".join(

            c if c.isalnum() else "_" for c in str(scope_name)

        )

        filename = f"{report_type}_{safe_scope}_{report_id}.pdf"

        file_path = REPORTS_DIR / filename

        with open(file_path, "wb") as pdf_file:

            pdf_file.write(pdf_bytes)

        self._log_report({

            "report_id": report_id,

            "report_type": report_type,

            "label": label,

            "scope_name": str(scope_name),

            "filename": filename,

            "generated_at": datetime.now(timezone.utc).isoformat()

        })

        data_logger.info(

            "Report generated",

            extra={"extra_data": {

                "report_id": report_id,

                "report_type": report_type,

                "scope": str(scope_name)

            }}

        )

        return pdf_bytes, filename, label

    # ============================================================
    # History Log
    # ============================================================

    def _log_report(self, entry: dict):

        entries = self._read_log()

        entries.append(entry)

        with open(REPORTS_LOG_PATH, "w", encoding="utf-8") as log_file:

            json.dump(entries, log_file, indent=2)

    def _read_log(self):

        if not REPORTS_LOG_PATH.exists():

            return []

        try:

            with open(REPORTS_LOG_PATH, "r", encoding="utf-8") as log_file:

                return json.load(log_file)

        except (json.JSONDecodeError, OSError):

            return []

    def get_report_history(self):

        entries = self._read_log()

        return sorted(

            entries,

            key=lambda entry: entry.get("generated_at", ""),

            reverse=True

        )

    def get_report_file_path(self, report_id: str):

        entries = self._read_log()

        match = next(

            (e for e in entries if e["report_id"] == report_id),

            None

        )

        if not match:

            raise ReportNotFoundError("Report not found.")

        file_path = REPORTS_DIR / match["filename"]

        if not file_path.exists():

            raise ReportNotFoundError("Report file no longer exists.")

        return file_path, match["filename"]

    def delete_report(self, report_id: str):

        entries = self._read_log()

        match = next(

            (e for e in entries if e["report_id"] == report_id),

            None

        )

        if not match:

            raise ReportNotFoundError("Report not found.")

        file_path = REPORTS_DIR / match["filename"]

        if file_path.exists():

            file_path.unlink()

        remaining = [

            e for e in entries if e["report_id"] != report_id

        ]

        with open(REPORTS_LOG_PATH, "w", encoding="utf-8") as log_file:

            json.dump(remaining, log_file, indent=2)

        return True
