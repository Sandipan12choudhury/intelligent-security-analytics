"""
==============================================================================
Reports API

Purpose
-------
Generate and retrieve Application / Department / Enterprise PDF
security reports.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response, FileResponse

from backend.models.report_models import GenerateReportRequest
from backend.services.report_service import ReportService, ReportNotFoundError

router = APIRouter(

    prefix="/api/v1/reports",

    tags=["Reports"]

)

service = ReportService()


# ============================================================
# Report History
# ============================================================

@router.get("/")

def report_history():

    return {

        "reports": service.get_report_history()

    }


# ============================================================
# Generate a New Report
# (returns the PDF directly, and saves a copy to history)
# ============================================================

@router.post("/generate")

def generate_report(request: GenerateReportRequest):

    try:

        pdf_bytes, filename, label = service.generate_report(

            request.report_type,

            request.scope

        )

    except ReportNotFoundError as error:

        raise HTTPException(status_code=404, detail=str(error))

    except ValueError as error:

        raise HTTPException(status_code=400, detail=str(error))

    return Response(

        content=pdf_bytes,

        media_type="application/pdf",

        headers={

            "Content-Disposition": f'attachment; filename="{filename}"'

        }

    )


# ============================================================
# Re-download a Historic Report
# ============================================================

@router.get("/download/{report_id}")

def download_report(report_id: str):

    try:

        file_path, filename = service.get_report_file_path(report_id)

    except ReportNotFoundError as error:

        raise HTTPException(status_code=404, detail=str(error))

    return FileResponse(

        path=str(file_path),

        media_type="application/pdf",

        filename=filename

    )


# ============================================================
# Delete a Report
# ============================================================

@router.delete("/{report_id}")

def delete_report(report_id: str):

    try:

        service.delete_report(report_id)

    except ReportNotFoundError as error:

        raise HTTPException(status_code=404, detail=str(error))

    return {"success": True}
