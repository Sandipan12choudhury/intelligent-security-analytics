"""
==============================================================================
Logs API

Purpose
-------
Read-only access to the application's own log files, so logged-in
users can monitor activity from within the app itself instead of
needing server/SSH access.

Author
------
Sandipan Choudhury
==============================================================================
"""

import json

from fastapi import APIRouter, Depends, HTTPException, Query

from backend.auth_dependency import get_current_user
from backend.logging_config import LOGS_DIR

router = APIRouter(

    prefix="/api/v1/logs",

    tags=["Logs"]

)

CATEGORY_FILES = {

    "app": "app.log",

    "auth": "auth.log",

    "data": "data.log"

}


@router.get("/{category}")

def get_logs(

    category: str,

    limit: int = Query(100, le=500),

    user_id: int = Depends(get_current_user)

):

    if category not in CATEGORY_FILES:

        raise HTTPException(

            status_code=404,

            detail="Unknown log category. Use app, auth, or data."

        )

    log_path = LOGS_DIR / CATEGORY_FILES[category]

    if not log_path.exists():

        return {"entries": []}

    with open(log_path, "r", encoding="utf-8") as log_file:

        lines = log_file.readlines()[-limit:]

    entries = []

    for line in reversed(lines):

        line = line.strip()

        if not line:

            continue

        try:

            entries.append(json.loads(line))

        except json.JSONDecodeError:

            entries.append({"message": line, "level": "RAW"})

    return {"entries": entries}
