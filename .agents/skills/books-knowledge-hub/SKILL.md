---
name: books-knowledge-hub
description: Query, search, extract engineering playbooks, audit polyglot SAST/OSV/SBOM/SARIF security, and discover GitHub repositories, AI tools, hardware designs, and tutorials learned from the 8,600+ compiled 5-Tier Books (`pipeline_data/books/Book_Context_<id>.md` & `Book_Lit_<id>.md`) via the `ChronicleRAG` (`chronicle-rag`) 55-Tool MCP server (`mcp_server.py`) backed by Unified PostgreSQL 17 (`pgvector` + `Apache AGE` + `TimescaleDB`).
---

# ChronicleRAG Books Knowledge Hub (`mcp_server.py` — 55 MCP Tools · Unified PostgreSQL 17 `pgvector` + `Apache AGE` + `TimescaleDB`)

> **MANDATORY `RULE-13` & `RULE-16` (`ChronicleRAG`-First Retrieval Gate & Zero-Runtime-ChromaDB Invariant)**:
> 1. **Query `ChronicleRAG` First**: Before running broad `Grep`/`Glob` workspace scans or `search_web` in any SetMiddle project, query `ChronicleRAG` first (`search_books`, `extract_learned_playbook`, `query_graphrag`, `query_code_map`, `query_workspace_graph`, or `read_book` in `compact=True` `< 10 KB` mode).
> 2. **Continue Seamlessly When Missing (`continue_if_missing`)**: If `ChronicleRAG` returns `abstention_triggered: false` and sufficient coverage, apply the learned playbook directly. If project-specific live symbols or lines are missing (`abstention_triggered: true` or partial coverage), automatically continue to: **(a) `Graphify` (`graphify query/path/explain`)** $\rightarrow$ **(b) Targeted `read_file` (`StartLine`..`EndLine`)** $\rightarrow$ **(c) External `search_web`**.
> 3. **Unified PostgreSQL 17 Storage (`RULE-16`)**: Runtime `chromadb` is retired across `ChronicleRAG` and SetMiddle in favor of Unified PostgreSQL 17 (`:5432/chroniclerag` and `:5433/chroniclerag`: `pgvector` HNSW + `Apache AGE` Cypher graph + `TimescaleDB` hypertables).

Use this skill whenever the user asks to apply knowledge, tools, repositories, patterns, security audits, polyglot language selection, or tutorials from the 8,600+ compiled 5-Tier Video & Literature Books (`pipeline_data/books/Book_Context_<id>.md`, `pipeline_data/books/Book_Lit_<id>.md`, and `books/master_books/Book_Lit_Master_*.md`).

## 1. Fast Book Learning, Tri-Factor Search & Playbook Extraction (`mcp_server.py`)

1. **`search_books(query, domain=None, limit=10)`**
   - Multi-field BM25 + **Generative Agents Tri-Factor Scoring** ($\text{Relevance} + \text{Recency} + \text{Importance}$) + MMR diversification ($\lambda=0.82$) across 8,600+ compiled books (`Book_Context_<id>.md`, `Book_Lit_<id>.md`, and Unified PostgreSQL 17 / `chronicle_records.jsonl`).
2. **`read_book(identifier, section="all")`**
   - Reads the full 5-Tier Book (`section="all" | "synopsis" | "chapters" | "audiobook" | "sfx" | "forensics" | "causal" | "metadata"`).
3. **`extract_learned_playbook(topic_or_task, max_books=12)`**
   - Synthesizes an actionable **Antigravity Learned Playbook** + **Polyglot Workload-to-Language Fitness Matrix** from all books matching `topic_or_task`.
4. **`find_tools_and_repos_in_books(query=None, domain=None, limit=50)`**
   - Lists GitHub repositories (`github.com/...`), AI plugins, CLI tools, and technical websites extracted across the library.
5. **`list_books_catalog(domain=None, search=None, limit=40, offset=0)`**
   - Returns the 16-category domain taxonomy breakdown and paginated catalog of all compiled books.

## 2. 5-Mode Unified GraphRAG (HippoRAG 2 PPR, Spectral $\lambda_2$, IIT 4.0 $\Phi_{\text{syn}}$ & Active Inference $G(\pi)$)

6. **`query_graphrag(query, mode="auto", max_results=8, return_json=False)`**
   - Unified **5-Mode GraphRAG Engine** routed by **Active Inference Expected Free Energy ($G(\pi)$)**:
     - `mode="pathrag"`: Flow-based path pruning with distance decay ($\alpha = 0.82$).
     - `mode="hipporag"`: **HippoRAG 2 Recognition-Memory + Inverse-Degree Specificity ($\deg(v)^{-0.35}$) Personalized PageRank (PPR)** ($\alpha = 0.85$).
     - `mode="community"`: **Hierarchical Community GraphRAG** executive cluster reports with **Fiedler Algebraic Connectivity ($\lambda_2$)** and **IIT 4.0 Integrated Information ($\Phi_{\text{syn}}$)**.
     - `mode="causal_dag"`: **Temporal-Causal State-Transition DAG** extracting chronological chapter transitions and quantitative specs.
     - `mode="dual_level"`: **LightRAG Dual-Level** retrieval combining High-Level architectural patterns with Low-Level concrete repos, symbols, and hardware pins.
7. **`query_pathrag(query, max_paths=8, max_hops=3, return_json=False)`**
8. **`get_graphrag_communities(domain=None, query=None)`**

## 3. Cross-Modal Polyglot AST Code Map (`Rust`, `Go`, `TS/JS`, `C/C++`, `Python`, `Java`, `C#`)

9. **`map_codebase(path_or_url=".", max_files=40)`**
   - Builds or surgically patches an **AST Code & Structural Symbol Map Book (`Book_Lit_*.md`)** for a local workspace or remote GitHub repository (`#Lstart-Lend`, classes, functions, polyglot call edges, and `.env` variables).
10. **`query_code_map(query, mode="auto", top_k=8)`**
    - Queries the Cross-Modal AST Code & Symbol Map, returning `#Lstart-Lend` clickable links, Call-Graph Blast Radius, `.env` usages (`os.getenv`, `std::env::var`, `os.Getenv`, `process.env`), and God Nodes.
11. **`sync_github_books(book_id_or_url="")`**
    - Surgically patches only modified GitHub repository chapters via Git `blob_sha` diffing.

## 4. Polyglot Language Matrix & Universal SAST / OSV / CycloneDX SBOM / SARIF 2.1.0 Security

12. **`sync_polyglot_language_matrix(force_online=False, ingest_official_release_docs=False, topic_or_task="")`**
    - Synchronizes live language versions & EOL dates from `endoflife.date` (`Rust`, `Go`, `C++20/23`, `TypeScript`, `Java`, `C#/.NET`, `Python`) and returns the workload-aware **Polyglot Language Fitness Matrix** (eliminating Python-by-default bias).
13. **`sync_vulnerability_advisories(force_online=True, max_kev_items=25)`**
    - Pulls live actively exploited CVEs from the **CISA KEV Catalog**, combines them with MITRE CWE Top 25, OWASP Top 10 (Web/API/LLM 2025), and polyglot advisory rules (`RustSec`, `GoVuln`, `PyPA`, `OSV.dev`), and compiles `Book_Lit_Vulnerability_Intelligence_Feed.md`.
14. **`scan_projects_for_vulnerabilities(target_path=".", scan_all_sibling_projects=False, check_osv_online=False)`**
    - Runs the 2-Phase Universal Polyglot SAST (**20 CWE & OWASP LLM Top 10 rules** across Python, Rust, Go, TypeScript/JS, C/C++, Java/Kotlin, C#, Solidity, YAML/Docker with **AST `enclosing_symbol` & `upstream_callers_in_file` Blast-Radius Pinpointing**) + SHA-256 Prior-Art Merkle Root + OSV.dev Batch CVE Lookup with **Execution-Model Reachability Filtering** (`_annotate_osv_reachability`).
15. **`generate_cyclonedx_sbom(target_path=".", include_osv_vulns=False)`**
    - Exports an EU Cyber Resilience Act (CRA) / NIS2 compliant **CycloneDX 1.5 SBOM** JSON manifest (`pipeline_data/sbom_cyclonedx_<project>.json`) with canonical Package URLs (`purl`), SHA-256 Merkle Root attestation, and reachability-annotated OSV status.
16. **`export_sarif_security_report(target_path=".", include_osv_vulns=False)`**
    - Exports an OASIS **SARIF 2.1.0** report (`pipeline_data/sarif_report_<project>.sarif.json`) across all 20 SAST rules with AST `logicalLocations` and a **100-Point ISO/IEC 25010 Security Readiness Scorecard**.
17. **`sync_antigravity_skills_to_all_projects(include_all_ide_workspaces=True, target_project_dir="")`**
    - Synchronizes ChronicleRAG's latest `.agents/skills/*` (`books-knowledge-hub`, `ux-engine`, `cybersecurity-backend-architecture`, `system-design-distributed-architecture`, and domain-matched Master Playbooks) across all Antigravity / IDE projects (`PycharmProjects`, `RustroverProjects`, `CLionProjects`, `IdeaProjects`, `WebstormProjects`).

## 5. Multimodal Ingestion, Audio/SFX, Multi-Voice Audiobooks, ComfyUI, 3D, Sovereign Failure Ledger & Closed-Loop Pipeline

18. **`ingest_file_to_rag`** | 19. **`ingest_directory_to_rag`** | 20. **`ingest_real_book`** | 21. **`ingest_webpage_or_wiki`** | 22. **`ingest_youtube_playlist`** | 23. **`analyze_reel`** | 24. **`sync_whatsapp_books`** | 25. **`generate_video_book_chronicle`** | 26. **`ask_causal_video_question`** | 27. **`analyze_audio_events_and_timings`** | 28. **`synthesize_audiobook`** | 29. **`analyze_vocal_prosody_and_omnivoice`** | 30. **`align_bimodal_book_and_audio_or_subtitles`** | 31. **`render_storyboard_via_comfyui`** | 32. **`compare_audiobook_with_comfyui`** | 33. **`generate_code_first_3d_scene_or_explainer`** | 34. **`compile_book_to_3d_didactic_lesson_or_cad`** | 35. **`compile_master_thematic_book`** | 36. **`export_master_book_to_project`** | 37. **`export_specialist_skill_and_sft_dataset`** | 38. **`compile_pass_through_book`** | 39. **`sync_learning_account`** | 40. **`hydrate_book_with_agent_failover`** | 41. **`verify_and_localize_book`** | 42. **`re_evaluate_book_with_new_eyes`** | 43. **`resolve_work_constellation`** | 44. **`list_work_constellations`** | 45. **`ingest_legal_open_seed_corpus`** | 46. **`reprocess_and_enrich_library`** | 47. **`search_reels`** | 48. **`extract_diagram_schema`** | 49. **`list_research_partitions`** | 50. **`list_analyzed_reels`** | 51. **`get_hardware_status`** | 52. **`log_sovereign_agent_failure`** | 53. **`distill_weekly_agent_failure_rules`** | 54. **`query_workspace_graph`** | 55. **`run_pedagogical_closed_loop_cycle`**.
