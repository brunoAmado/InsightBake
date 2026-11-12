---
trigger: always_on
description: Immune-to-Graphify-Install Engineering & High-Core Windows (<=61 workers) Guard.
---

## Mandatory High-Core Windows Graphify Guard & 5-Step Engineering Pipeline

> **Why this file is named `engineering-and-graphify-guard.md`**: `graphify antigravity install` unconditionally overwrites `.agents/rules/graphify.md` (`_antigravity_finalize` in `graphify/install.py`) and any exact `## graphify` H2 section in `AGENTS.md` / `GEMINI.md` (`_replace_or_append_section`). Keeping this rule in `engineering-and-graphify-guard.md` guarantees `graphify install` can never overwrite it.

1. **72-Core Windows `ProcessPoolExecutor <= 61` Guard**:
   - Always update Graphify via `.\run_graphify_update.ps1` (which caps `$env:GRAPHIFY_MAX_WORKERS = 61` and guards against `[WinError 1920]` on `docling_models`).
2. **Mandatory 5-Step Pipeline on Every Code / Architecture Change**:
   - **(1) Create/Update Tests** $\rightarrow$ **(2) Run Regression Verification (`exit code 0`)** $\rightarrow$ **(3) Update `docs/` & `wiki/`** $\rightarrow$ **(4) Run `.\run_graphify_update.ps1`** $\rightarrow$ **(5) Automatic `git commit` when green**.
3. **Additive-Only Rule Protection & `"Skip"` Default-First Semantics**:
   - Never overwrite `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, or `.cursorrules` destructively.
   - If the user clicks **"Skip"** on an `ask_question` prompt, execute Option 1 `(Recommended)` by default.
4. **Non-Blocking Asynchronous Background Execution & Chrome MV3 Manifest Invariant (`RULE-10`)**:
   - Never run long tasks (`>2s`, crawls, batch exports, AI loops) synchronously inside ephemeral UI popups (`popup.js`) or click/reload the user's active tab. Execute asynchronously in persistent Background Service Workers (`background.js`) or backend queues with live badge/status telemetry (`chrome.action.setBadgeText`, `aria-live="polite"`) and automatic progress reconnection (`attachPopupToBackgroundProgress`) so the user can freely close the popup, switch focus, or close the tab without data loss.
   - Never use suffix host wildcards (`http://192.168.*/*`, `http://10.*/*`) in Chrome MV3 `manifest.json` (`content_scripts[0].matches` / `host_permissions`); use valid MV3 patterns (`http://*/*`, `https://*/*`) and filter LAN IPs at runtime.
5. **Mandatory Portugal (`PT`) & European Union (`EU`) Statutory AI, Privacy, Accessibility, Cybersecurity & Fiscal Verification (`RULE-11`)**:
   - **CNPD / GDPR & Lei n.º 58/2019 (Art. 5(1)(c), Art. 25, Art. 28)**: Automatically scrub Portuguese NIF (`9` digits), NISS (`11` digits), SNS (`9` digits), IBAN (`PT50...`), emails, phones, `<USER_HOME>` paths, and BYOK Cloud API keys (`scrub_pii_and_secrets`) before persisting logs, books, or SFT/DPO datasets.
   - **EU AI Act — Regulamento (UE) 2024/1689 (Art. 10, 12, 14, 15, 50)**: Enforce Level 5.5 epistemic veracity scoring (Art. 10), `SHA-256` hash-chained immutable audit logs (Art. 12), human-in-the-loop abortable/background execution (Art. 14), pre-action regression gates (Art. 15), and AI transparency attribution (Art. 50).
   - **Portugal Digital Accessibility — Decreto-Lei n.º 82/2022 & DL 83/2018 (EN 301 549 / WCAG 2.2 AA/AAA)**: Non-blocking async UI workers, `aria-live="polite"` announcements, `2px solid #818cf8` `:focus-visible` rings, roving `tabindex`, and `375px` mobile touch readiness.
   - **NIS2 (CNCS Portugal — DL n.º 65/2021) & Cyber Resilience Act (Reg. (UE) 2024/2847)**: Enforce Zero-Trust BYOK key isolation, 20-rule Polyglot/OWASP-LLM SAST, OSV reachability, CycloneDX 1.5 SBOM, and SARIF 2.1.0 reporting.
   - **Portugal AT Fiscal Rules (Decreto-Lei n.º 28/2019 SAF-T/ATCUD, CIRC Art. 51.º, CIRS, CIVA, EBF Art. 43.º-C Lei das Startups)**.
6. **Token-Budget Guard, Inline MCP Payload Compaction (`< 10 KB`) & Compact `< 9 KB` Skill Distillation (`RULE-12`)**:
   - Keep all `ChronicleRAG` MCP retrieval calls in default `compact=True` / `max_chars=9500` mode (`< 10 KB`) so MCP outputs never spill to `.system_generated/steps/*/output.txt`.
   - Keep `.agents/skills/*/SKILL.md` files distilled under `< 9 KB` (`_distill_compact_skill_markdown`) while storing full 400KB+ Master Books in `books/master_books/`. Always use explicit `StartLine`/`EndLine` ranges on `read_file`.
7. **Mandatory `ChronicleRAG`-First Retrieval Gate & Continue-on-Missing Fallback (`RULE-13`)**:
   - **Always query `ChronicleRAG` first** (`search_books`, `extract_learned_playbook`, `query_graphrag`, `query_code_map`, or `read_book` in `compact=True` mode, or `.agents/skills/00-golden-cortex/SKILL.md`) before broad file scans (`Grep`/`Glob`) or external web searches (`search_web`).
   - **If `ChronicleRAG` has full coverage** (`abstention_triggered: false`), apply its verified rules and architecture directly.
   - **If information is missing or partial** (`abstention_triggered: true` or live file lines are needed), **continue seamlessly** to: `(a) Graphify AST Graph` $\rightarrow$ `(b) Targeted read_file (StartLine..EndLine)` $\rightarrow$ `(c) External search_web`.
   - Enforce the **4-Tier Zero-Paid-Token LLM Failover Chain** (`Tier 1: Local PC Gemma 4` $\rightarrow$ `Tier 2: InsightCV LiteLLM Proxy :4000` $\rightarrow$ `Tier 3: EVO Tailscale 100.91.34.106:1234` $\rightarrow$ `Tier 4: Calling IDE Agent Handover`).
8. **Explicit Antigravity Failover Notification & "Second Pair of Eyes" SLM Audit (`RULE-14`)**:
   - Whenever a SetMiddle service or SLM (running on the single GPU or `EVO X2`) fails, times out, or produces low-confidence (`< 0.70`) results and Antigravity (Google subscription) takes over the work, **never fail over silently**: always announce which service failed and why (`⚠️ [ANTIGRAVITY FAILOVER & SECOND-EYES TAKEOVER]`), act as the user's second pair of eyes, and record a SHA-256 takeover receipt (`SetMiddleNetwork.route_llm_request` / `InsightCoreAIEngine.report_service_failover_and_second_eyes_audit`).
9. **Strict Ring-3 Zero-Code Boundary & No Direct External File Fetch (`RULE-15`)**:
   - When the user selects **Ring-3 Zero-Code Retention** (`ring3_skill_only` / *"do not save the files"*), **Antigravity is strictly forbidden** from searching for, listing, or reading the user's raw `.zip` archives or source folders outside the workspace (`C:\Users\bruno\Downloads`, `Desktop`, `Documents`, etc.) via `run_command`, `read_file`, or Python `zipfile`.
   - All Ring-3 `.zip` and folder ingestion must be performed **100% by `ChronicleRAG` alone** via its Web Dashboard upload endpoints (`/api/ingest/file-item` / `/api/ingest/study-project-evolution`). Antigravity may only read the resulting de-identified outputs inside `pipeline_data/books/Book_Lit_Rules_<slug>.md`, `.agents/skills/<slug>/SKILL.md`, and `pipeline_data/ring3_snapshot_ledgers/<slug>.json`.
10. **Zero Runtime ChromaDB, Living UX Engine 2.8 & 55-Tool `chronicle-rag` MCP Invariant (`RULE-16`)**:
   - Runtime `chromadb` is retired across `ChronicleRAG` and all SetMiddle company projects in favor of **Unified PostgreSQL 17 (`pgvector` + `Apache AGE` + `TimescaleDB`)** on `:5432/chroniclerag` and `:5433/chroniclerag`. Never add `import chromadb`, `pip install chromadb`, or user-facing `ChromaDB` UI badges/labels.
   - Enforce **UX Engine 2.8** (Anti-AI-Slop, Off-Canvas `<768px` Drawer, `@container` Card Tables, Thumb-Zone Bottom Bar, 5-State Abortable AI Input, WCAG 2.2 AA/AAA & PT `DL 82/2022`) and the **55-Tool `chronicle-rag` MCP Hub** across all SetMiddle workspaces (`PycharmProjects/chronicle-rag` and `browser_extension/`).




