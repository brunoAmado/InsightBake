"""
Unit, Unhappy-Path & Regression Tests for `SetMiddle Insight™ · Bake` (`InsightBake` / `insight_bake`).
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fastapi.testclient import TestClient
from insight_bake.engine import InsightBakeEngine
from insight_bake.server import app


class TestInsightBake(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = InsightBakeEngine()
        self.client = TestClient(app)

    def test_01_health_status_and_3d_studio_ui(self) -> None:
        r_health = self.client.get("/health")
        self.assertEqual(r_health.status_code, 200)
        self.assertEqual(r_health.json()["service"], "InsightBake")
        self.assertEqual(r_health.json()["port"], 4030)

        r_status = self.client.get("/api/bake/status")
        self.assertEqual(r_status.status_code, 200)
        self.assertTrue(r_status.json()["ok"])

        r_studio = self.client.get("/api/bake/studio")
        self.assertEqual(r_studio.status_code, 200)
        self.assertIn("SetMiddle Insight™ · Bake", r_studio.text)

    def test_02_design_3d_cake_portions_dowels_bom_allergens_and_controlnet(self) -> None:
        r_des = self.client.post(
            "/api/bake/design",
            json={
                "shape": "ROUND",
                "tiers": [
                    {"diameter_cm": 30.0, "height_cm": 12.0},
                    {"diameter_cm": 22.0, "height_cm": 12.0},
                    {"diameter_cm": 15.0, "height_cm": 14.0},
                ],
                "sponge_key": "chocolate_belga_70",
                "filling_key": "praline_avela_crocante",
                "frosting_key": "ganache_blindagem_fondant",
                "topper_text": "Inês & João",
            },
        )
        self.assertEqual(r_des.status_code, 200)
        body = r_des.json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["threejs_3d_scene"]["tier_count"], 3)
        self.assertEqual(body["threejs_3d_scene"]["total_height_cm"], 38.0)
        self.assertGreater(body["portions_and_structure"]["wedding_portions_2_5x5cm"], 100)
        self.assertEqual(len(body["portions_and_structure"]["tier_dowel_blueprint"]), 2)
        self.assertIn("NUTS", body["allergens_eu_1169_2011"]["allergen_codes"])
        self.assertGreater(body["pricing_and_at_invoicing"]["recommended_client_total_gross_eur"], 150.0)
        self.assertEqual(body["comfyui_controlnet_render"]["controlnet_depth_strength"], 0.88)

    def test_03_unhappy_path_inverted_tier_binary_blob_and_pii_scrub(self) -> None:
        # Unstable inverted tier (30cm stacked on top of 15cm) must be rejected
        r_inv = self.client.post(
            "/api/bake/design",
            json={"tiers": [{"diameter_cm": 15.0, "height_cm": 12.0}, {"diameter_cm": 30.0, "height_cm": 12.0}]},
        )
        self.assertEqual(r_inv.status_code, 400)
        self.assertIn("INVERTED_UNSTABLE_TIER", r_inv.json()["error"])

        # Binary blob rejected
        bad_blob = self.engine.execute({"raw_blob": "data:image/png;base64," + ("A" * 600)})
        self.assertFalse(bad_blob["ok"])
        self.assertEqual(bad_blob["error"], "BINARY_BLOB_REJECTED_USE_CAS_URI")

        # PII scrubbed
        r_scrub = self.client.post("/api/bake/scrub", json={"text": "Cliente NIF 123456789"})
        self.assertEqual(r_scrub.status_code, 200)
        self.assertNotIn("123456789", r_scrub.json()["scrubbed_text"])


if __name__ == "__main__":
    unittest.main()
