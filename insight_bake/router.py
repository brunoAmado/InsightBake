"""
FastAPI `APIRouter` Plugin for `SetMiddle Insight™ · Bake` (`insight_bake.router`).
Can be mounted standalone (`:4030`) or inside `ChronicleRAG` (`:8765`).
"""

from typing import Any, Dict
from fastapi import APIRouter, Body, FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response

from insight_bake.engine import InsightBakeEngine


INTERACTIVE_3D_CAKE_STUDIO_HTML = """<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SetMiddle Insight™ · Bake — 3D Cake &amp; Pastry Configurator + ControlNet Studio</title>
<style>
  body { background:#090d16; color:#f8fafc; font-family:Inter,system-ui,sans-serif; margin:0; padding:20px; font-variant-numeric:tabular-nums; }
  .layout { display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:18px; max-width:1280px; margin:0 auto; }
  .card { background:#172033; border:1px solid rgba(255,255,255,0.08); border-radius:16px; padding:18px; }
  h1 { font-size:22px; margin:0 0 6px; color:#f8fafc; }
  h2 { font-size:15px; margin:0 0 12px; color:#818cf8; text-transform:uppercase; letter-spacing:0.05em; }
  label { display:block; font-size:13px; color:#cbd5e1; margin:10px 0 4px; font-weight:500; }
  select, input { width:100%; box-sizing:border-box; background:#0f172a; color:#f8fafc; border:1px solid #334155; border-radius:10px; padding:10px; font-size:16px; }
  button.primary { background:#4f46e5; color:#fff; border:none; border-radius:10px; padding:12px 18px; font-size:15px; font-weight:600; cursor:pointer; width:100%; margin-top:14px; }
  button.primary:hover { background:#4338ca; }
  :focus-visible { outline:2px solid #818cf8; outline-offset:2px; }
  .kpi-row { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-top:12px; }
  .kpi { background:#0f172a; border:1px solid rgba(255,255,255,0.06); border-radius:10px; padding:10px; text-align:center; }
  .kpi b { display:block; font-size:20px; color:#38bdf8; }
  .kpi span { font-size:11px; color:#94a3b8; }
  #cake-svg-stage { width:100%; height:320px; background:radial-gradient(circle at 50% 35%, #1e293b, #090d16); border-radius:12px; display:flex; align-items:center; justify-content:center; }
  pre { background:#0f172a; padding:10px; border-radius:8px; font-size:12px; overflow-x:auto; color:#a5b4fc; }
</style>
</head>
<body>
<a href="#main-content" style="position:absolute;left:-9999px;">Saltar para o conteúdo principal</a>
<main id="main-content" aria-live="polite" style="max-width:1280px;margin:0 auto;">
  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;margin-bottom:16px;">
    <div>
      <span style="font-size:11px;background:#312e81;color:#c7d2fe;padding:4px 10px;border-radius:999px;font-weight:600;">SETMIDDLE INSIGHT™ PRODUCT LINE · INTERNAL ENGINE: INSIGHTCORE</span>
      <h1 style="margin-top:8px;">🎂 SetMiddle Insight™ · Bake — Estúdio 3D de Cake Design, Receituário &amp; Logística Frio</h1>
    </div>
  </div>
  <div class="layout">
    <section class="card" aria-label="Configurador 3D do Bolo">
      <h2>1. Configurar Andares, Sabores &amp; Topo</h2>
      <label for="sponge-sel">Massa do Bolo (Sponge)</label>
      <select id="sponge-sel">
        <option value="red_velvet">Red Velvet Artisanal (Buttermilk &amp; Cacau)</option>
        <option value="pao_de_lo_tradicional">Pão de Ló Tradicional Português</option>
        <option value="chocolate_belga_70">Bolo Húmido de Chocolate Belga 70%</option>
        <option value="amendoa_sem_gluten">Bolo de Amêndoa &amp; Limão (Sem Glúten)</option>
      </select>
      <label for="filling-sel">Recheio (Filling)</label>
      <select id="filling-sel">
        <option value="brigadeiro_gourmet">Brigadeiro Gourmet de Chocolate Nobre</option>
        <option value="ovos_moles_doces_conventuais">Doce de Ovos Conventual Português</option>
        <option value="curd_limao_frutos_vermelhos">Lemon Curd &amp; Frutos Vermelhos</option>
        <option value="praline_avela_crocante">Ganache &amp; Praliné de Avelã</option>
      </select>
      <label for="frosting-sel">Cobertura &amp; Estrutura (Frosting)</label>
      <select id="frosting-sel">
        <option value="swiss_meringue_buttercream">Swiss Meringue Buttercream (Lambeth / Cetim)</option>
        <option value="ganache_blindagem_fondant">Blindagem em Ganache + Pasta de Açúcar (Fondant)</option>
        <option value="semi_naked_rustico">Semi-Naked Rústico com Flores Naturais</option>
      </select>
      <label for="topper-inp">Texto do Topo (Topper Acrílico)</label>
      <input id="topper-inp" type="text" value="Sofia &amp; Miguel" />
      <button type="button" class="primary" onclick="recalcCake()">Calcular Estrutura 3D, Receita (g), Preço (€) &amp; Render IA</button>
    </section>

    <section class="card" aria-label="Visualização 3D e Fatias">
      <h2>2. Pré-Visualização 3D &amp; Engenharia de Suporte (Estacas)</h2>
      <div id="cake-svg-stage">
        <svg viewBox="0 0 300 260" width="280" height="250" role="img" aria-label="Modelo 3D de Bolo de 3 Andares">
          <text x="150" y="28" text-anchor="middle" fill="#facc15" font-size="13" font-weight="bold" id="svg-topper">✨ Sofia &amp; Miguel ✨</text>
          <rect x="105" y="40" width="90" height="52" rx="8" fill="#fffdf9" stroke="#d4af37" stroke-width="2.5"/>
          <rect x="82" y="92" width="136" height="60" rx="8" fill="#fffdf9" stroke="#d4af37" stroke-width="2.5"/>
          <rect x="55" y="152" width="190" height="68" rx="8" fill="#fffdf9" stroke="#d4af37" stroke-width="2.5"/>
          <ellipse cx="150" cy="224" rx="115" ry="10" fill="#475569"/>
        </svg>
      </div>
      <div class="kpi-row">
        <div class="kpi"><b id="kpi-portions">105</b><span>Fatias Casamento</span></div>
        <div class="kpi"><b id="kpi-weight">9.4 kg</b><span>Peso Total</span></div>
        <div class="kpi"><b id="kpi-price">€248.50</b><span>Preço c/ IVA (50% Sinal)</span></div>
      </div>
    </section>

    <section class="card" aria-label="Ficha Técnica, Alergénios, ComfyUI e Transporte Frio">
      <h2>3. Ficha de Produção (g), Alergénios (ASAE) &amp; Prompt ComfyUI ControlNet</h2>
      <pre id="production-json">Clique em "Calcular Estrutura 3D" para gerar a ficha completa...</pre>
    </section>
  </div>
</main>
<script>
async function recalcCake() {
  const payload = {
    sponge_key: document.getElementById('sponge-sel').value,
    filling_key: document.getElementById('filling-sel').value,
    frosting_key: document.getElementById('frosting-sel').value,
    topper_text: document.getElementById('topper-inp').value
  };
  document.getElementById('svg-topper').textContent = '✨ ' + payload.topper_text + ' ✨';
  const r = await fetch('/api/bake/design', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(payload)});
  const data = await r.json();
  if (data.ok) {
    document.getElementById('kpi-portions').textContent = data.portions_and_structure.wedding_portions_2_5x5cm;
    document.getElementById('kpi-weight').textContent = data.portions_and_structure.total_assembled_weight_kg + ' kg';
    document.getElementById('kpi-price').textContent = '€' + data.pricing_and_at_invoicing.recommended_client_total_gross_eur;
    document.getElementById('production-json').textContent = JSON.stringify({
      recipe_bom_grams: data.recipe_bom_grams,
      dowels: data.portions_and_structure.tier_dowel_blueprint,
      allergens: data.allergens_eu_1169_2011.allergen_codes,
      cold_chain_fleet: data.logistics_and_haccp_cold_chain,
      comfyui_controlnet_prompt: data.comfyui_controlnet_render.positive_prompt
    }, null, 2);
  }
}
recalcCake();
</script>
</body>
</html>"""


def create_insight_bake_router() -> APIRouter:
    engine = InsightBakeEngine()
    router = APIRouter(tags=["InsightBake"])

    @router.get("/status")
    def get_status() -> Dict[str, Any]:
        return engine.get_status()

    @router.get("/studio", response_class=HTMLResponse)
    def get_interactive_3d_studio() -> HTMLResponse:
        return HTMLResponse(content=INTERACTIVE_3D_CAKE_STUDIO_HTML)

    @router.post("/design")
    @router.post("/execute")
    def execute_action(payload: Dict[str, Any] = Body(default={})) -> JSONResponse:
        res = engine.execute(payload)
        return JSONResponse(status_code=200 if res.get("ok") else 400, content=res)

    @router.post("/scrub")
    def scrub_text(payload: Dict[str, Any] = Body(default={})) -> Dict[str, Any]:
        return engine.scrub_input(str(payload.get("text", "")))

    @router.get("/widget.js")
    def get_web_component_js() -> Response:
        js = """
(function() {
  if (typeof window === 'undefined' || customElements.get('insight-bake')) return;
  class CustomWidgetElement extends HTMLElement {
    connectedCallback() {
      const apiBase = this.getAttribute('api-base') || '/api/bake';
      this.innerHTML = `<section role="region" aria-label="SetMiddle Insight™ · Bake" style="background:#0f172a;color:#f8fafc;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:16px;font-family:Inter,system-ui,sans-serif;"><h3 style="margin:0;font-size:15px;font-weight:600;">SetMiddle Insight™ · Bake (3D Cake &amp; Pastry Studio)</h3><div aria-live="polite" style="font-size:12px;color:#94a3b8;margin-top:6px;font-variant-numeric:tabular-nums;">Active on ${apiBase} · Three.js 3D + ComfyUI ControlNet + HACCP Cold-Chain · Powered by InsightCore</div></section>`;
    }
  }
  customElements.define('insight-bake', CustomWidgetElement);
})();
""".strip()
        return Response(content=js, media_type="application/javascript")

    return router


def mount_insight_bake_plugin(app: FastAPI, prefix: str = "/api/bake") -> bool:
    app.include_router(create_insight_bake_router(), prefix=prefix)
    return True
