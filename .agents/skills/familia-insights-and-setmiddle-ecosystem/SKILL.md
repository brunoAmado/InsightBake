---
name: familia-insights-and-setmiddle-ecosystem
description: Compact Team Master Playbook for Familia Insights and SetMiddle Ecosystem distilled from ChronicleRAG (Book_Lit_Master_Familia_Insights_and_SetMiddle_Ecosystem.md). Enforces core architectural, UI/UX, and implementation rules with <9KB context footprint.
---

# ⚡ Compact Specialist Skill: Familia Insights and SetMiddle Ecosystem (`lit_Master_Familia_Insights_and_SetMiddle_Ecosystem`)
> **Token-Budget Guard (`RULE-12`)**: This skill is pre-distilled (`< 9 KB`) from `books/master_books/Book_Lit_Master_Familia_Insights_and_SetMiddle_Ecosystem.md` (`30 KB`) to prevent context bloat.
> **Active SetMiddle Ecosystem Baseline (`RULE-10..RULE-16`)**: **UX Engine 2.8** · **Unified PostgreSQL 17 (`pgvector` + `Apache AGE` + `TimescaleDB` on `:5432/:5433`, Zero Runtime `ChromaDB`)** · **55-Tool `chronicle-rag` MCP Hub** · **WCAG 2.2 AA/AAA & PT `DL 82/2022`**.
> **Hierarchical Progressive Disclosure & Backtrace**:
> - **Full Chapter TOC**: `chronicle-rag:read_book(identifier='lit_Master_Familia_Insights_and_SetMiddle_Ecosystem', section='toc')`
> - **Surgical Single Chapter + Origin Backtrace**: `chronicle-rag:read_book(identifier='lit_Master_Familia_Insights_and_SetMiddle_Ecosystem', section='chapter:<N>')` or `section='chapter:<keyword>'`
> - **Recursive 'New Eyes' Critique**: `chronicle-rag:read_book(identifier='lit_Master_Familia_Insights_and_SetMiddle_Ecosystem', section='new_eyes')`

## 🌟 Executive Synopsis: 10 Cross-Project Architectural Laws Learned from the 17 Repositories
1. **4-Layer Hybrid Polyglot Standard**: Every standalone product ships `rust_core/` (memory-safe crypto/math/interlocks) + `firmware/` or `node_sdk/` + `Python FastAPI Service & Mountable Router` + `ui_component/` (`CustomElement` Web Component with Shadow DOM).
2. **Dual Deployment Topology (`DEMO_SHARED` vs `CLIENT_PROD`)**: Every module runs either as an isolated microservice (`:4001`–`:4009`, `:8050`, `:8080`, `:8095`, `:8096`) or mounted as a zero-overhead router inside `ChronicleRAG` (`:8765`).
3. **Centralized Networking & 4-Tier Zero-Paid-Token LLM Proxy (`SetMiddleNetwork:4008`)**: All projects route LLM/VLM/Embedding calls through `CHIMERA` LiteLLM Proxy (`100.107.21.79:4000/v1`) -> `CHIMERA` vLLM (`:8011/v1`) -> `EVO` GPU Client (`100.91.34.106:1234/v1`) -> `IDE Agent Handover`.

## 📐 Distilled Engineering Rules & Actionable Patterns
