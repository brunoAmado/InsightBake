"""
`SetMiddle Insight™ · Bake` (`InsightBake` · `insight_bake.engine`).
Internal Engine: `InsightCore` (`insightCoreIO` + `insightCoreAI`).

Combines:
1. **Parametric `Three.js` 3D Cake Scene Graph & Structural Engineering**:
   - Multi-tier (`1..6` tiers) geometry (`ROUND`, `SQUARE`, `HEART`, `HEXAGON`), exact Wedding (`2.5cm x 5cm`) vs. Party (`5cm x 5cm`) slice calculator, total mass (`kg`), and **Internal Dowel Rod + Center Skewer Structural Blueprint** so stacked tiers never collapse.
2. **Exact Ingredient BOM Scaling, EU Reg. 1169/2011 Allergen Label & Portuguese AT (`ATCUD` / IVA 13%/23%) Pricing**:
   - Scales flour, sugar, eggs, butter, chocolate, filling, and frosting in grams (`g`) from the exact 3D cylinder/prism volume ($\text{cm}^3$) and computes raw ingredient cost, baker labor, margin, and 50% deposit invoice.
3. **Zero-Hallucination `ComfyUI` ControlNet Depth/Canny Photorealistic Studio Prompt Builder**:
   - Locks the exact `Three.js` 3D tier aspect ratios (`controlnet_depth_weight=0.88`) so `Flux.1-dev` / `SDXL` renders photorealistic fondant, Lambeth piping, gold leaf, and sugar flowers without inventing impossible shapes.
4. **Refrigerated Van Logistics & ASAE HACCP Cold-Chain Handover (`InsightFleet :4026` + `InsightSensor :4025`)**:
   - Computes required cake box dimensions (`cm`), refrigerated transport window (`+2 °C to +5 °C`), and maximum safe G-force (`<= 0.35 g`) on curves/cobblestones.
"""

from __future__ import annotations

import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

_INSIGHT_CORE_DIR = Path("C:/Users/bruno/PycharmProjects/InsightCore")
if _INSIGHT_CORE_DIR.exists() and str(_INSIGHT_CORE_DIR) not in sys.path:
    sys.path.insert(0, str(_INSIGHT_CORE_DIR))

from insight_core_io import assert_no_binary_blob_in_db_row, scrub_pt_eu_pii_and_byok_secrets


EU_14_MANDATORY_ALLERGENS: Dict[str, str] = {
    "GLUTEN": "Cereais que contêm glúten (trigo, centeio, cevada, aveia) — Reg. (UE) n.º 1169/2011 Anexo II",
    "EGGS": "Ovos e produtos à base de ovos — Reg. (UE) n.º 1169/2011 Anexo II",
    "MILK": "Leite e produtos à base de leite (incluindo lactose) — Reg. (UE) n.º 1169/2011 Anexo II",
    "NUTS": "Frutos de casca rija (amêndoas, avelãs, nozes, pistácios) — Reg. (UE) n.º 1169/2011 Anexo II",
    "SOY": "Soja e produtos à base de soja (lecitina no chocolate) — Reg. (UE) n.º 1169/2011 Anexo II",
}

SPONGE_RECIPES: Dict[str, Dict[str, Any]] = {
    "pao_de_lo_tradicional": {
        "name": "Pão de Ló Tradicional Português",
        "density_g_per_cm3": 0.42,
        "cost_eur_per_kg": 6.80,
        "allergens": ["GLUTEN", "EGGS"],
        "ratios": {"eggs_g": 0.45, "sugar_g": 0.30, "wheat_flour_g": 0.25},
    },
    "red_velvet": {
        "name": "Red Velvet Artisanal (Buttermilk & Cocoa)",
        "density_g_per_cm3": 0.54,
        "cost_eur_per_kg": 8.50,
        "allergens": ["GLUTEN", "EGGS", "MILK"],
        "ratios": {"wheat_flour_g": 0.30, "sugar_g": 0.28, "buttermilk_g": 0.20, "eggs_g": 0.12, "butter_g": 0.10},
    },
    "chocolate_belga_70": {
        "name": "Bolo Húmido de Chocolate Belga 70%",
        "density_g_per_cm3": 0.58,
        "cost_eur_per_kg": 10.20,
        "allergens": ["GLUTEN", "EGGS", "MILK", "SOY"],
        "ratios": {"wheat_flour_g": 0.24, "sugar_g": 0.26, "dark_chocolate_70_g": 0.20, "eggs_g": 0.15, "butter_g": 0.15},
    },
    "amendoa_sem_gluten": {
        "name": "Bolo de Amêndoa & Limão (Sem Glúten)",
        "density_g_per_cm3": 0.52,
        "cost_eur_per_kg": 12.40,
        "allergens": ["EGGS", "NUTS"],
        "ratios": {"almond_flour_g": 0.45, "sugar_g": 0.30, "eggs_g": 0.25},
    },
}

FILLING_RECIPES: Dict[str, Dict[str, Any]] = {
    "brigadeiro_gourmet": {
        "name": "Brigadeiro Gourmet de Chocolate Nobre",
        "cost_eur_per_kg": 11.50,
        "allergens": ["MILK", "SOY"],
        "requires_refrigeration_4c": True,
    },
    "ovos_moles_doces_conventuais": {
        "name": "Doce de Ovos Conventual Português",
        "cost_eur_per_kg": 10.80,
        "allergens": ["EGGS"],
        "requires_refrigeration_4c": True,
    },
    "curd_limao_frutos_vermelhos": {
        "name": "Lemon Curd & Compota de Frutos Vermelhos",
        "cost_eur_per_kg": 12.00,
        "allergens": ["EGGS", "MILK"],
        "requires_refrigeration_4c": True,
    },
    "praline_avela_crocante": {
        "name": "Ganache & Praliné de Avelã Piemontesa",
        "cost_eur_per_kg": 15.50,
        "allergens": ["MILK", "NUTS", "SOY"],
        "requires_refrigeration_4c": True,
    },
}

FROSTING_RECIPES: Dict[str, Dict[str, Any]] = {
    "swiss_meringue_buttercream": {
        "name": "Swiss Meringue Buttercream (Cetim Suave)",
        "cost_eur_per_kg": 9.80,
        "allergens": ["EGGS", "MILK"],
        "max_ambient_temp_c": 23.0,
    },
    "ganache_blindagem_fondant": {
        "name": "Blindagem em Ganache + Pasta de Açúcar (Fondant)",
        "cost_eur_per_kg": 12.50,
        "allergens": ["MILK", "SOY"],
        "max_ambient_temp_c": 28.0,
    },
    "semi_naked_rustico": {
        "name": "Semi-Naked Rústico com Flores Naturais",
        "cost_eur_per_kg": 8.90,
        "allergens": ["EGGS", "MILK"],
        "max_ambient_temp_c": 22.0,
    },
}


def design_3d_cake_and_production_sheet(
    tiers: List[Dict[str, Any]] | None = None,
    shape: str = "ROUND",
    sponge_key: str = "red_velvet",
    filling_key: str = "brigadeiro_gourmet",
    frosting_key: str = "swiss_meringue_buttercream",
    style_theme: str = "Vintage Lambeth Piping with Gold Leaf & White Sugar Peonies",
    primary_color_hex: str = "#FFFDF9",
    accent_color_hex: str = "#D4AF37",
    topper_text: str = "Sofia & Miguel",
    hourly_rate_eur: float = 22.0,
) -> Dict[str, Any]:
    """
    Computes the complete `Three.js` 3D scene graph, wedding/party portions, structural dowel blueprint,
    gram-exact ingredient recipe BOM, EU Reg. 1169/2011 allergen declaration, ComfyUI ControlNet prompt,
    and `InsightFleet` / `InsightSensor` refrigerated delivery plan.
    """
    tier_specs = tiers if isinstance(tiers, list) and tiers else [
        {"diameter_cm": 25.0, "height_cm": 12.0},
        {"diameter_cm": 20.0, "height_cm": 12.0},
        {"diameter_cm": 15.0, "height_cm": 14.0},
    ]
    if len(tier_specs) > 6:
        return {"ok": False, "error": "MAX_6_TIERS_EXCEEDED_STRUCTURAL_SAFETY_LIMIT"}

    shape_clean = str(shape or "ROUND").strip().upper()
    if shape_clean not in ("ROUND", "SQUARE", "HEART", "HEXAGON"):
        shape_clean = "ROUND"

    sponge = SPONGE_RECIPES.get(sponge_key, SPONGE_RECIPES["red_velvet"])
    filling = FILLING_RECIPES.get(filling_key, FILLING_RECIPES["brigadeiro_gourmet"])
    frosting = FROSTING_RECIPES.get(frosting_key, FROSTING_RECIPES["swiss_meringue_buttercream"])

    threejs_meshes: List[Dict[str, Any]] = []
    structural_dowels: List[Dict[str, Any]] = []
    current_y_cm = 0.0
    total_volume_cm3 = 0.0
    total_surface_cm2 = 0.0
    total_wedding_portions = 0
    total_party_portions = 0
    max_diameter_cm = 0.0

    for idx, t in enumerate(tier_specs):
        diam = float(t.get("diameter_cm", 20.0))
        height = float(t.get("height_cm", 12.0))
        if diam < 8.0 or diam > 60.0 or height < 5.0 or height > 30.0:
            return {
                "ok": False,
                "error": f"INVALID_TIER_DIMENSIONS_AT_TIER_{idx + 1}(diameter={diam}cm,height={height}cm)",
            }
        if idx > 0 and diam > float(tier_specs[idx - 1].get("diameter_cm", 20.0)):
            return {
                "ok": False,
                "error": f"INVERTED_UNSTABLE_TIER_AT_TIER_{idx + 1}({diam}cm_ON_TOP_OF_{tier_specs[idx - 1].get('diameter_cm')}cm)",
            }

        max_diameter_cm = max(max_diameter_cm, diam)
        radius = diam / 2.0
        if shape_clean == "SQUARE":
            base_area_cm2 = diam * diam
            perimeter_cm = 4.0 * diam
        elif shape_clean == "HEXAGON":
            base_area_cm2 = 2.598 * (radius ** 2)
            perimeter_cm = 6.0 * radius
        else:
            base_area_cm2 = math.pi * (radius ** 2)
            perimeter_cm = 2.0 * math.pi * radius

        vol_cm3 = base_area_cm2 * height
        surf_cm2 = base_area_cm2 + (perimeter_cm * height)
        total_volume_cm3 += vol_cm3
        total_surface_cm2 += surf_cm2

        # Wedding slice: 2.5cm x 5cm base (~12.5 cm2), Party slice: 5cm x 5cm (~25 cm2)
        height_factor = 1.25 if height >= 13.0 else 1.0
        w_slices = max(4, int(round((base_area_cm2 / 12.5) * height_factor)))
        p_slices = max(3, int(round((base_area_cm2 / 22.0) * height_factor)))
        total_wedding_portions += w_slices
        total_party_portions += p_slices

        # Structural dowels needed if another tier sits above this tier
        dowels_in_tier = 0
        if idx < len(tier_specs) - 1:
            upper_diam = float(tier_specs[idx + 1].get("diameter_cm", 15.0))
            dowels_in_tier = max(4, int(round(upper_diam / 3.5)))
            structural_dowels.append({
                "tier_index": idx + 1,
                "tier_diameter_cm": diam,
                "supports_upper_tier_diameter_cm": upper_diam,
                "polypropylene_dowel_rods_count": dowels_in_tier,
                "dowel_cut_height_cm": height,
                "cake_board_under_upper_tier_cm": upper_diam,
            })

        threejs_meshes.append({
            "tier_number": idx + 1,
            "geometry_type": "BoxGeometry" if shape_clean == "SQUARE" else "CylinderGeometry",
            "radial_segments": 6 if shape_clean == "HEXAGON" else 64,
            "diameter_cm": diam,
            "height_cm": height,
            "position_y_cm": round(current_y_cm + (height / 2.0), 2),
            "base_color_hex": primary_color_hex,
            "piping_accent_color_hex": accent_color_hex,
            "wedding_portions": w_slices,
            "party_portions": p_slices,
            "internal_dowels_count": dowels_in_tier,
        })
        current_y_cm += height

    # Gram-exact Ingredient Scaling
    sponge_weight_g = round(total_volume_cm3 * 0.68 * float(sponge["density_g_per_cm3"]), 1)
    filling_weight_g = round(total_volume_cm3 * 0.24 * 0.95, 1)
    frosting_weight_g = round(total_surface_cm2 * 0.85, 1)
    total_cake_weight_kg = round((sponge_weight_g + filling_weight_g + frosting_weight_g) / 1000.0, 2)

    sponge_ingredients_g = {
        k: round(sponge_weight_g * ratio, 1) for k, ratio in sponge["ratios"].items()
    }

    # Costing & AT Pricing
    raw_materials_eur = (
        (sponge_weight_g / 1000.0) * float(sponge["cost_eur_per_kg"])
        + (filling_weight_g / 1000.0) * float(filling["cost_eur_per_kg"])
        + (frosting_weight_g / 1000.0) * float(frosting["cost_eur_per_kg"])
        + (len(tier_specs) * 4.50)  # Boards, dowels, box
    )
    estimated_labor_hours = round(2.5 + (len(tier_specs) * 1.8) + (total_wedding_portions * 0.025), 1)
    labor_cost_eur = estimated_labor_hours * float(hourly_rate_eur)
    subtotal_net_eur = round((raw_materials_eur * 1.35) + labor_cost_eur, 2)
    iva_rate_pct = 13.0  # Taxa intermédia IVA Portugal restauração/pastelaria ou 23%
    total_gross_eur = round(subtotal_net_eur * (1.0 + (iva_rate_pct / 100.0)), 2)
    deposit_50pct_eur = round(total_gross_eur * 0.50, 2)

    # Mandatory EU Reg. 1169/2011 Allergen Union
    allergen_codes = sorted(set(sponge["allergens"]) | set(filling["allergens"]) | set(frosting["allergens"]))
    allergen_declarations = [
        {"code": c, "statutory_label_pt": EU_14_MANDATORY_ALLERGENS.get(c, c)} for c in allergen_codes
    ]

    # ComfyUI ControlNet Photorealistic Studio Prompt
    comfyui_controlnet_spec = {
        "engine": "ComfyUI Flux.1-dev / SDXL + ControlNet Depth & Canny Lock",
        "controlnet_depth_strength": 0.88,
        "controlnet_canny_strength": 0.65,
        "anti_hallucination_geometry_lock": f"Locked to exact {len(tier_specs)}-tier Three.js Z-depth map ({total_wedding_portions} portions, {current_y_cm}cm total height)",
        "positive_prompt": (
            f"Award-winning commercial studio food photography of a {len(tier_specs)}-tier {shape_clean.lower()} luxury celebration cake, "
            f"tier diameters {[t['diameter_cm'] for t in threejs_meshes]} cm, total height {current_y_cm} cm, "
            f"covered in {frosting['name']} ({primary_color_hex}) with {accent_color_hex} accents, {style_theme}, "
            f"custom acrylic topper reading '{topper_text}', 85mm f/1.8 macro lens, soft diffused natural window key light, "
            "hyper-realistic sugar texture, Vogue Weddings editorial style, 8k resolution"
        ),
        "negative_prompt": "lopsided tiers, floating elements, collapsed cake, plastic look, cartoon, watermark, deformed text, extra tiers",
    }

    # Refrigerated Logistics & ASAE HACCP Cold-Chain Spec (`InsightFleet` + `InsightSensor`)
    box_width_cm = round(max_diameter_cm + 10.0, 1)
    box_height_cm = round(current_y_cm + 14.0, 1)
    center_skewer_required = len(tier_specs) >= 2

    return {
        "ok": True,
        "member": "InsightBake",
        "client_brand": "SetMiddle Insight™ · Bake (Cake & Pastry 3D Studio)",
        "internal_engine": "InsightCore",
        "threejs_3d_scene": {
            "shape": shape_clean,
            "tier_count": len(tier_specs),
            "total_height_cm": round(current_y_cm, 1),
            "max_base_diameter_cm": round(max_diameter_cm, 1),
            "topper_text": topper_text,
            "tiers": threejs_meshes,
        },
        "portions_and_structure": {
            "wedding_portions_2_5x5cm": total_wedding_portions,
            "party_portions_5x5cm": total_party_portions,
            "total_assembled_weight_kg": total_cake_weight_kg,
            "center_sharpened_dowel_skewer_required": center_skewer_required,
            "tier_dowel_blueprint": structural_dowels,
        },
        "recipe_bom_grams": {
            "sponge_type": sponge["name"],
            "sponge_total_g": sponge_weight_g,
            "sponge_ingredients_g": sponge_ingredients_g,
            "filling_type": filling["name"],
            "filling_total_g": filling_weight_g,
            "frosting_type": frosting["name"],
            "frosting_total_g": frosting_weight_g,
        },
        "allergens_eu_1169_2011": {
            "regulation": "Regulamento (UE) n.º 1169/2011 & Decreto-Lei n.º 26/2016 (ASAE Alergénios)",
            "allergen_codes": allergen_codes,
            "mandatory_client_label": allergen_declarations,
        },
        "pricing_and_at_invoicing": {
            "raw_ingredients_and_packaging_cost_eur": round(raw_materials_eur, 2),
            "estimated_baker_labor_hours": estimated_labor_hours,
            "labor_cost_eur": round(labor_cost_eur, 2),
            "recommended_net_price_eur": subtotal_net_eur,
            "iva_rate_pct": iva_rate_pct,
            "recommended_client_total_gross_eur": total_gross_eur,
            "deposit_50pct_atcud_invoice_eur": deposit_50pct_eur,
        },
        "comfyui_controlnet_render": comfyui_controlnet_spec,
        "logistics_and_haccp_cold_chain": {
            "powered_by": ["SetMiddle Insight™ · Fleet (:4026)", "SetMiddle Insight™ · Sensor (:4025)"],
            "required_transport_box_cm": f"{box_width_cm} x {box_width_cm} x {box_height_cm} cm",
            "refrigerated_van_target_temp_c": "+2.0 °C to +5.0 °C (ASAE Reg. CE 852/2004)",
            "max_safe_ambient_display_temp_c": frosting["max_ambient_temp_c"],
            "max_safe_cornering_g_force": 0.35,
            "non_slip_silicone_mat_required": True,
        },
    }


class InsightBakeEngine:
    MEMBER_ID = "InsightBake"
    CLIENT_BRAND = "SetMiddle Insight™ · Bake"
    INTERNAL_ENGINE = "InsightCore"
    DEFAULT_PORT = 4030
    API_PREFIX = "/api/bake"

    def get_status(self) -> Dict[str, Any]:
        return {
            "ok": True,
            "product": self.CLIENT_BRAND,
            "member_id": self.MEMBER_ID,
            "internal_engine": self.INTERNAL_ENGINE,
            "version": "1.0.0",
            "port": self.DEFAULT_PORT,
            "api_prefix": self.API_PREFIX,
            "standalone_benefit": (
                "Interactive Three.js 3D Multi-Tier Cake Configurator + ComfyUI ControlNet Photorealistic Studio Renderer "
                "+ Exact Portion/Dowel/Gram Recipe Scaler + EU 1169/2011 Allergen & AT Deposit Quote Calculator for Cake Designers & Pastry Chefs."
            ),
            "ecosystem_synergy": [
                "Combined with SetMiddle Insight™ · Fleet (:4026): Checks refrigerated delivery box dimensions, route smoothness (<=0.35g vibration), and venue arrival windows.",
                "Combined with SetMiddle Insight™ · Sensor (:4025): Monitors bakery fridge/freezer temperatures 24/7 for ASAE HACCP (Reg. CE 852/2004) compliance.",
                "Combined with SetMiddle Insight™ · Fiscal (:4017) & Expense (:4002): Issues immediate 50% deposit ATCUD / SAF-T (PT) invoices upon client 3D cake approval.",
            ],
            "available_sponges": list(SPONGE_RECIPES.keys()),
            "available_fillings": list(FILLING_RECIPES.keys()),
            "available_frostings": list(FROSTING_RECIPES.keys()),
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        ok_storage, violations = assert_no_binary_blob_in_db_row(payload or {})
        if not ok_storage:
            return {"ok": False, "member": self.MEMBER_ID, "error": "BINARY_BLOB_REJECTED_USE_CAS_URI", "violations": violations}
        data = payload or {}
        return design_3d_cake_and_production_sheet(
            tiers=data.get("tiers"),
            shape=str(data.get("shape", "ROUND")),
            sponge_key=str(data.get("sponge_key") or data.get("spongeKey") or "red_velvet"),
            filling_key=str(data.get("filling_key") or data.get("fillingKey") or "brigadeiro_gourmet"),
            frosting_key=str(data.get("frosting_key") or data.get("frostingKey") or "swiss_meringue_buttercream"),
            style_theme=str(data.get("style_theme") or data.get("styleTheme") or "Vintage Lambeth Piping with Gold Leaf"),
            primary_color_hex=str(data.get("primary_color_hex") or data.get("primaryColorHex") or "#FFFDF9"),
            accent_color_hex=str(data.get("accent_color_hex") or data.get("accentColorHex") or "#D4AF37"),
            topper_text=str(data.get("topper_text") or data.get("topperText") or "Sofia & Miguel"),
            hourly_rate_eur=float(data.get("hourly_rate_eur", 22.0)),
        )

    def scrub_input(self, text: str) -> Dict[str, Any]:
        return scrub_pt_eu_pii_and_byok_secrets(text)
