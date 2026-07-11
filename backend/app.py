"""
==============================================================================
FastAPI Application

Purpose
-------
Entry point of the Intelligent Security Analytics Platform.

Responsibilities
----------------
• Create FastAPI application
• Configure middleware
• Register API routers
• Expose REST endpoints

Author
------
Sandipan Choudhury
==============================================================================
"""

import os
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.api.artifacts import router as artifact_router
from backend.api.dashboard import router as dashboard_router
from backend.api.applications import router as application_router
from backend.api.observations import router as observation_router
from backend.api.export import router as export_router
from backend.api.reports import router as report_router
from backend.api.auth import router as auth_router
from backend.api.logs import router as logs_router

from backend.logging_config import app_logger

# =============================================================================
# FastAPI Application
# =============================================================================

app = FastAPI(

    title="Intelligent Security Analytics Platform",

    description="Enterprise AI Platform for Security Assessment Automation",

    version="1.0.0"

)

# =============================================================================
# CORS Configuration
# =============================================================================

_default_origins = "http://localhost:5173"

_allowed_origins = os.getenv("ALLOWED_ORIGINS", _default_origins)

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        origin.strip() for origin in _allowed_origins.split(",")

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# =============================================================================
# Request Logging Middleware
# =============================================================================

@app.middleware("http")

async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    duration_ms = round((time.time() - start_time) * 1000, 2)

    app_logger.info(

        f"{request.method} {request.url.path} -> {response.status_code}",

        extra={"extra_data": {

            "method": request.method,

            "path": request.url.path,

            "status_code": response.status_code,

            "duration_ms": duration_ms

        }}

    )

    return response

# =============================================================================
# Register Routers
# =============================================================================

app.include_router(artifact_router)
app.include_router(dashboard_router)
app.include_router(application_router)
app.include_router(observation_router)
app.include_router(export_router)
app.include_router(report_router)
app.include_router(auth_router)
app.include_router(logs_router)

# =============================================================================
# Root Endpoint
# =============================================================================

@app.get("/")

def home():

    return {

        "application": "Intelligent Security Analytics Platform",

        "version": "1.0.0",

        "status": "Running"

    }

# =============================================================================
# Health Check
# =============================================================================

@app.get("/health")

def health():

    return {

        "status": "Healthy"

    }