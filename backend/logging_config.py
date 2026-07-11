"""
==============================================================================
Logging Configuration

Purpose
-------
Three separate, size-capped log files, each holding structured
(JSON-line) entries so they're easy to both read and parse back for
the in-app log viewer:

    logs/app.log   - every HTTP request (method, path, status, timing)
    logs/auth.log  - security events (login, register, password/
                     username changes, account deletion, failures)
    logs/data.log  - data events (observation created, report
                     generated)

Each file is capped at 5 MB with 3 rotated backups, so log files
never grow without bound.

Usage
-----
    from backend.logging_config import auth_logger

    auth_logger.info(
        "Login succeeded",
        extra={"extra_data": {"username": username, "user_id": user_id}}
    )

Author
------
Sandipan Choudhury
==============================================================================
"""

import json
import logging
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOGS_DIR = PROJECT_ROOT / "logs"

LOGS_DIR.mkdir(exist_ok=True)

MAX_LOG_BYTES = 5 * 1024 * 1024

BACKUP_COUNT = 3


class JsonFormatter(logging.Formatter):

    def format(self, record):

        payload = {

            "timestamp": datetime.now(timezone.utc).isoformat(),

            "level": record.levelname,

            "message": record.getMessage()

        }

        extra_data = getattr(record, "extra_data", None)

        if extra_data:

            payload.update(extra_data)

        return json.dumps(payload)


def _build_logger(name: str, filename: str) -> logging.Logger:

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        handler = RotatingFileHandler(

            LOGS_DIR / filename,

            maxBytes=MAX_LOG_BYTES,

            backupCount=BACKUP_COUNT

        )

        handler.setFormatter(JsonFormatter())

        logger.addHandler(handler)

        logger.propagate = False

    return logger


app_logger = _build_logger("app", "app.log")

auth_logger = _build_logger("auth", "auth.log")

data_logger = _build_logger("data", "data.log")
