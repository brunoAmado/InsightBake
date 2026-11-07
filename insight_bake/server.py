"""
Standalone FastAPI Server for `SetMiddle Insight™ · Bake` (`python -m insight_bake.server`).
Runs on port 4030 by default.
"""

import os
import sys
from pathlib import Path
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from insight_bake.router import INTERACTIVE_3D_CAKE_STUDIO_HTML, mount_insight_bake_plugin

app = FastAPI(
    title="SetMiddle Insight™ · Bake (InsightBake) — Three.js 3D Multi-Tier Cake Configurator, ComfyUI ControlNet Studio, Recipe BOM & HACCP Cold-Chain Logistics (Powered by InsightCore)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

mount_insight_bake_plugin(app, prefix="/api/bake")


@app.get("/", response_class=HTMLResponse)
@app.get("/dashboard", response_class=HTMLResponse)
def standalone_project_dashboard() -> HTMLResponse:
    """Serves the standalone UX Engine 2.8 & WCAG 2.2 AA/AAA webpage & interactive 3D Cake Studio."""
    ic_dir = "C:/Users/bruno/PycharmProjects/InsightCore"
    if Path(ic_dir).exists() and ic_dir not in sys.path:
        sys.path.insert(0, ic_dir)
    try:
        from insight_core.dashboard_ui import render_standalone_project_dashboard_html
        return HTMLResponse(content=render_standalone_project_dashboard_html("InsightBake", host_mode="STANDALONE"))
    except Exception:
        return HTMLResponse(content=INTERACTIVE_3D_CAKE_STUDIO_HTML)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "InsightBake",
        "client_brand": "SetMiddle Insight™ · Bake",
        "internal_engine": "InsightCore",
        "port": 4030,
        "api_prefix": "/api/bake",
        "version": "1.0.0",
    }


def main() -> None:
    port = int(os.environ.get("PORT", "4030"))
    uvicorn.run(app, host="127.0.0.1", port=port)


if __name__ == "__main__":
    main()
