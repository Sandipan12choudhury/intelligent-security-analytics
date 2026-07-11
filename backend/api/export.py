"""
==============================================================================
Export API

Purpose
-------
REST endpoint that turns an observation + its generated AI artifacts
into a downloadable CSV, PDF, or Word file.

Author
------
Sandipan Choudhury
==============================================================================
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from backend.models.export_models import ExportRequest
from backend.services.export_service import ExportService

router = APIRouter(

    prefix="/api/v1/export",

    tags=["Export"]

)

service = ExportService()

MEDIA_TYPES = {

    "csv": "text/csv",

    "pdf": "application/pdf",

    "docx":
        "application/vnd.openxmlformats-officedocument"
        ".wordprocessingml.document"

}


@router.post("/{file_format}")

def export_observation(file_format: str, request: ExportRequest):

    file_format = file_format.lower()

    if file_format not in MEDIA_TYPES:

        raise HTTPException(

            status_code=400,

            detail=(
                "Unsupported export format. "
                "Use one of: csv, pdf, docx."
            )

        )

    if file_format == "csv":

        content = service.to_csv(request)

    elif file_format == "pdf":

        content = service.to_pdf(request)

    else:

        content = service.to_docx(request)

    filename = f"{request.observation_id}_ai_report.{file_format}"

    return Response(

        content=content,

        media_type=MEDIA_TYPES[file_format],

        headers={

            "Content-Disposition":
                f'attachment; filename="{filename}"'

        }

    )
