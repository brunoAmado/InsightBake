/**
 * SetMiddle Insight™ · Bake — Node.js / TypeScript SDK (`:4030 /api/bake`)
 */
export async function designCake3D(baseUrl = "http://127.0.0.1:4030", payload = {}) {
  const res = await fetch(`${baseUrl}/api/bake/design`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}
