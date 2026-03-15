"""Minimal FastAPI app for the OTLP HTTP receiver on port 4318.

Shares the StreamingTraceManager with the main app (port 8001).
Mounts only the /v1/traces and /v1/logs endpoints.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .otlp_routes import otlp_router, set_trace_manager

otlp_app = FastAPI(title="agentevals OTLP receiver")

otlp_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

otlp_app.include_router(otlp_router)


@otlp_app.on_event("startup")
async def startup():
    from .app import get_trace_manager

    mgr = get_trace_manager()
    if mgr:
        set_trace_manager(mgr)
