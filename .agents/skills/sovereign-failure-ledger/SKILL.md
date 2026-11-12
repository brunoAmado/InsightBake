---
name: sovereign-failure-ledger
description: Sovereign Agent Failure Ledger, GDPR/CNPD PII Scrubber, and Weekly Failure-to-Rule Distiller learned from Book 2608398502964270 (The Faction Group LLC) and mined from 440+ local Antigravity sessions.
---

# ⚡ Compact Specialist Skill: Sovereign Agent Failure Ledger & Distilled Rules
> **Last Distilled**: `2026-11-03 13:32 UTC` | **Total Logged Incidents**: `343` | **PII/Secret Redactions**: `81`
> **Full Book**: `books/master_books/Book_Lit_Master_Sovereign_Agent_Failure_Ledger.md` (`chronicle-rag:read_book(identifier='lit_Sovereign_Agent_Failure_Ledger')`)

## 📑 Distilled Failure-to-Rule Gates (`RULE-01` .. `RULE-12`)
1. **`RULE-07-GENERAL-AGENT-EXECUTION-GUARD`** (236 incidents) — **General Execution & Pre-Condition Verification Failure**
   - *Rule*: Verify file existence, schema invariants, and command exit codes before chaining dependent operations, and attach a deterministic regression test to every fixed bug.
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
2. **`RULE-03-MCP-SYNC-TIMEOUT-AND-BACKGROUNDING`** (40 incidents) — **Long-Running Multimodal / Whisper / VLM Task Blocking Synchronous MCP Socket (`>180s`)**
   - *Rule*: Heavy multimodal pipelines (Whisper CUDA transcription + 40-frame DivX GPU OCR + VLM storyboarding) can exceed the 180s stdio MCP timeout. Check `pipeline_data/videos/<id>.meta.json` if already downloaded and run `DecoupledPipeline.process_single_video(meta)` asynchronously or with pre-flight VLM circuit-breaker checks.
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
3. **`RULE-01-POWERSHELL-SYNTAX-AND-VENV`** (34 incidents) — **Windows PowerShell vs. Bash Syntax & Venv Interpreter Mismatch**
   - *Rule*: On Windows (`pwsh`), always invoke project Python via `.\.venv\Scripts\python.exe` (never bare `python`), use `;` or native PowerShell pipelines (`Select-Object -First N`, `Get-ChildItem`) instead of POSIX `head`/`tail`/`grep`, and quote paths containing spaces.
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
4. **`RULE-02-API-SIGNATURE-AND-KWARG-VERIFICATION`** (8 incidents) — **Unverified Method Signature / Unexpected Keyword Argument (`TypeError` / `AttributeError`)**
   - *Rule*: Never guess Python/Rust/TS method signatures or keyword argument names from memory. Always inspect the function definition (`read_file` or `inspect.signature`) before invoking internal engine methods (e.g. `BOOK_ENGINE.set_book_classification(book_id, partition=..., classifications=..., tags=...)`).
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
5. **`RULE-08-WINDOWS-HIGH-CORE-GRAPHIFY-WORKERS`** (7 incidents) — **Windows High-Core CPU (>61 Logical Processors) `ProcessPoolExecutor` Crash in Graphify**
   - *Rule*: On high-core Windows PCs (>61 logical cores), Python's `ProcessPoolExecutor` raises `ValueError: max_workers must be <= 61`. Always run `.\run_graphify_update.ps1` or set `$env:GRAPHIFY_MAX_WORKERS = [math]::Min(61, [math]::Max(2, [int]($env:NUMBER_OF_PROCESSORS * 0.75)))` before `graphify update .`.
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
6. **`RULE-11-PT-EU-STATUTORY-AI-GOVERNANCE`** (6 incidents) — **Portugal (`PT`) & European Union (`EU`) Statutory AI, Privacy, Accessibility & Fiscal Verification Gate**
   - *Rule*: Enforce Portugal (`PT`) and European Union (`EU`) statutory rules across all AI & software projects: (1) CNPD / GDPR & Lei n.º 58/2019 (Art. 5(1)(c), Art. 25, Art. 28): automatic local redaction (`scrub_pii_and_secrets`) of NIF, NISS, SNS, IBAN PT50, emails, phones, home paths, and BYOK API keys before disk persistence; (2) EU AI Act (Regulamento (UE) 2024/1689 Art. 10, 12, 14, 15, 50): epistemic veracity scoring, SHA-256 hash-chained audit logs, human-in-the-loop abortable/background execution, pre-action regression gates, and AI transparency attribution; (3) Portugal Decreto-Lei n.º 82/2022 & DL 83/2018 (EN 301 549 / WCAG 2.2 AA/AAA): non-blocking async workers, `aria-live='polite'` status announcements, visible `:focus-visible` rings, roving `tabindex`, and 375px mobile readiness; (4) NIS2 (CNCS Portugal) & Cyber Resilience Act (Reg. (UE) 2024/2847): 20-rule Polyglot/OWASP-LLM SAST, OSV reachability, CycloneDX 1.5 SBOM, and SARIF 2.1.0; (5) Portugal AT Fiscal Rules (Decreto-Lei n.º 28/2019 SAF-T/ATCUD, CIRC Art. 51.º, CIRS, CIVA, EBF Art. 43.º-C Lei das Startups).
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
7. **`RULE-05-UNICODE-AND-WINDOWS-CONSOLE-ENCODING`** (4 incidents) — **Windows CP1252 / UTF-8 Console & JSONL Encoding Crash (`UnicodeEncodeError` / `UnicodeDecodeError`)**
   - *Rule*: Always specify `encoding='utf-8', errors='replace'` on all `Path.read_text()`, `Path.write_text()`, and `open()` calls on Windows, and use `ensure_ascii=False` when serializing JSON/JSONL.
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
8. **`RULE-06-USER-STEERING-AND-ANTI-MOCK-ISOLATION`** (4 incidents) — **User Steering Correction: Zero Mock Fallbacks & Production UX/Security Enforcement**
   - *Rule*: Never emit mock placeholder strings (`kubectl get pods`, fake data) into production records or books, never persist raw BYOK cloud keys to disk, and always enforce UX Engine 2.8 4-state completeness (`Loading`, `Empty`, `Error + Retry`, `Success`).
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
9. **`RULE-10-ASYNC-NON-BLOCKING-UI-AND-MV3-MANIFEST`** (2 incidents) — **Synchronous Ephemeral Popup Execution / Tab Reloading & Invalid Chrome MV3 Host Wildcards**
   - *Rule*: 1) In Chrome Manifest V3 (`manifest.json`), never use suffix host wildcards (`http://192.168.*/*`, `http://10.*/*`) in `content_scripts[0].matches`; use valid MV3 patterns (`http://*/*`, `https://*/*`) and filter LAN IPs at runtime. 2) Under Portugal Decreto-Lei n.º 82/2022 (WCAG 2.2 AA/AAA) & EU AI Act Art. 14/15, long-running browser or UI tasks (>2s) must NEVER run synchronously inside an ephemeral Popup (`popup.js`) or click/reload the user's active tab. Always execute asynchronously in the persistent Background Service Worker (`background.js`) or backend worker queue with live toolbar badge telemetry and progress reconnection (`attachPopupToBackgroundProgress`).
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
10. **`RULE-09-ADDITIVE-AGENTS-MD-AND-AUTO-COMMIT`** (1 incidents) — **Destructive `AGENTS.md` Rule Overwrite, Missing Test->Regression->Auto-Commit & `Skip` Prompt Cancel**
   - *Rule*: Never overwrite `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, or `.cursorrules` with a blanket template that drops existing rules—always merge additively. For every code change: (1) create/update tests, (2) run regression verification, (3) run `.\run_graphify_update.ps1`, and (4) automatically `git commit` when green without waiting to be asked. If `ask_question` is skipped by the user, treat Option 1 `(Recommended)` as the selected default.
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
11. **`RULE-12-TOKEN-BUDGET-AND-MCP-PAYLOAD-COMPACTION`** (1 incidents) — **MCP Output Spillover (`output.txt` >12KB), Bloated `.agents/skills/*/SKILL.md` (>12KB) & Quadratic Context Growth**
   - *Rule*: 1) Keep all MCP tool responses (`search_books`, `extract_learned_playbook`, `read_book`, `list_books_catalog`, `find_tools_and_repos_in_books`) below 10 KB by default (`compact=True`) so Antigravity never spills truncated MCP payloads to `.system_generated/steps/*/output.txt` and wastes 3-5 extra `read_file` turns. 2) Distill `.agents/skills/*/SKILL.md` files into compact (<12 KB) executive playbooks (`_distill_compact_skill_markdown`) while keeping full 400KB+ Master Books in `books/master_books/`. 3) Never read duplicate copies of the same UX Engine spec (`DESIGN.md` + `ux-engine/SKILL.md` + `Book_Lit_Master_UI_UX_Engineering.md` + `PLAYBOOK_UI_UX_ENGINEERING.md`) in the same turn.
   - *Gate*: `pytest tests/test_agent_failure_regression_gates.py`
