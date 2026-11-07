"""
`SetMiddle Insight™ · Bake` (`InsightBake` — `:4030 /api/bake`) — Extracted Domain Module powered by `InsightCore™`.
"""

from insight_bake.engine import (
    EU_14_MANDATORY_ALLERGENS,
    SPONGE_RECIPES,
    FILLING_RECIPES,
    FROSTING_RECIPES,
    InsightBakeEngine,
    design_3d_cake_and_production_sheet,
)
from insight_bake.router import create_insight_bake_router, mount_insight_bake_plugin

__version__ = "1.0.0"

__all__ = [
    "EU_14_MANDATORY_ALLERGENS",
    "SPONGE_RECIPES",
    "FILLING_RECIPES",
    "FROSTING_RECIPES",
    "InsightBakeEngine",
    "design_3d_cake_and_production_sheet",
    "__version__",
    "create_insight_bake_router",
    "mount_insight_bake_plugin",
]
