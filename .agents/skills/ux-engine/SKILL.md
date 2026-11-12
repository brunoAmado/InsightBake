---
name: ux-engine
description: Compact Team Master Playbook for UI UX Engineering distilled from ChronicleRAG (Book_Lit_Master_UI_UX_Engineering.md). Enforces core architectural, UI/UX, and implementation rules with <9KB context footprint.
---

# ⚡ Compact Specialist Skill: UI UX Engineering (`lit_Master_UI_UX_Engineering`)
> **Token-Budget Guard (`RULE-12`)**: This skill is pre-distilled (`< 9 KB`) from `books/master_books/Book_Lit_Master_UI_UX_Engineering.md` (`413 KB`) to prevent context bloat.
> **Active SetMiddle Ecosystem Baseline (`RULE-10..RULE-16`)**: **UX Engine 2.8** · **Unified PostgreSQL 17 (`pgvector` + `Apache AGE` + `TimescaleDB` on `:5432/:5433`, Zero Runtime `ChromaDB`)** · **55-Tool `chronicle-rag` MCP Hub** · **WCAG 2.2 AA/AAA & PT `DL 82/2022`**.
> **Hierarchical Progressive Disclosure & Backtrace**:
> - **Full Chapter TOC**: `chronicle-rag:read_book(identifier='lit_Master_UI_UX_Engineering', section='toc')`
> - **Surgical Single Chapter + Origin Backtrace**: `chronicle-rag:read_book(identifier='lit_Master_UI_UX_Engineering', section='chapter:<N>')` or `section='chapter:<keyword>'`
> - **Recursive 'New Eyes' Critique**: `chronicle-rag:read_book(identifier='lit_Master_UI_UX_Engineering', section='new_eyes')`

## 🎨 Canonical UX Engine 2.8 Non-Negotiables
1. **Anti-AI-Slop Dark Surfaces**: `#090d16` (`canvas`) -> `#0f172a` (`surface`) -> `#172033` (`card`), `tabular-nums`, `68ch` prose measure, Concentric Radii (`Inner = Outer - Padding`), 1 Primary CTA per view.
2. **UX Engine 2.8 Mobile & Layout**: Off-Canvas `<768px` Mobile Drawer, `@container` / `table.mobile-card-table` row collapse, `16px` mobile inputs (anti-iOS-zoom), `44x44px` coarse-pointer targets, `env(safe-area-inset-bottom)` thumb-zone bar, 5-State Abortable AI Chat Input, Live UX/WCAG 2.2 Self-Auditor.
3. **4 Async States + WCAG 2.2 AA/AAA + PT `DL 82/2022`**: Skeleton loading, Empty CTA, plain-language Error + `↻ Retry`, `<100ms` Success + `#sr-announcer` (`aria-live='polite'`), `2px solid #818cf8` `:focus-visible`, roving `tabindex`, modal `Tab` trap.

## 🌟 Executive Synopsis (Level 1)
Team-shared Master Thematic Book consolidating **111 chapters** and **89 source books** on `UI_UX_Engineering`.

## 📑 Key Chapters Index (Showing 25 of 879 Chapters)
- **Chapter 1**: Anti-AI-Slop Dashboard Architecture
- **Chapter 2**: Typography as a 7-Decision Mathematical System
- **Chapter 3**: Concentric Border Radii, Cards vs. Panels & Dark-Mode Elevation
- **Chapter 4**: Form UX, Validation Timing & Control Selection
- **Chapter 5**: Desktop Data Tables, Bulk Selection & Mobile Row Stacking
- **Chapter 6**: Cursor Pagination, URL State & Scroll Restoration
- **Chapter 7**: Modals vs. Sheets vs. Drawers, Command Palette (`⌘K`) & Context Menus
- **Chapter 8**: Perceived Instant Speed (Raycast Pattern), Skeleton CLS & Drag-and-Drop Physics
- **Chapter 9**: Danger Actions, 5s Soft-Delete Undo Toasts & Specific "Done" Screens
- **Chapter 10**: Defensive CSS for Real Data, Resizable Panels & Mobile Hover Guards
- **Chapter 11**: Zero-JS Modern CSS (`:has()`, `@container`, View Transitions & Scroll-Snap)
- **Chapter 12**: Micro-Component Polish: Clipboard, Avatars, Voice/Swipe Physics & Pricing UX
- **Chapter 13**: UX Engine 2.0 Architecture: `design-system`, `visual-character` 4-Axis Law & `/restyle`
- **Chapter 14**: Honest Dashboard Charts, Data Visualization & Pro Number Formatting
- **Chapter 15**: Specialized High-Conversion Inputs: AI Prompt Box, Stripe Checkout, Card, OTP, Password, Date Picker, Slider & Color Picker
- **Chapter 16**: Navigation Systems, 4-Level File Trees, Non-Jumping Tabs, Search, Filter Chips & Multi-Step Wizards
- **Chapter 17**: Reactive State Machines: Auto-Save, Optimistic UI, Button Click Lifecycle, Double-Tap Guard & Disabled Button Explanations
- **Chapter 18**: SaaS Workspace Systems: Linear Aesthetic, Chat Threads, 40-Event Calendar Week View, Settings Page, Notifications, Multiplayer & Z-Index Scale
- **Chapter 19**: Cognitive Psychology Laws, Organic Motion Timing, Golden Ratio & Anti-AI Landing Page Tells
- **Chapter 20**: UX Engine 2.4 (`375px` Mobile Readiness), Full Keyboard Navigation Architecture & WCAG 2.2 AA Accessibility
- **Chapter 21**: UX Engine 2.4: Effortless Search (5 Decisions), First-Run Onboarding (5 Pieces) & Permission Prompts (5 Rules)
- **Chapter 22**: UX Engine 2.5: Notion Zero-Friction Blank Canvas, Live Multi-Page Reactive Dashboards, Visual Diagnostic Matrix & Contrast Eye-Tracking
- **Chapter 23**: brunoAmado/chronicle-rag — README.md > **Source Link**: https://github.com/brunoAmado (🛡️ 9.5/10 | PT: 9.8/10)
- **Chapter 24**: Home (🛡️ 9.7/10 | PT: 9.9/10)
- **Chapter 25**: README > **Source Link**: J:/bobcat/bobcat300-recycle/README.md (🛡️ 9.1/10 | PT: 9.4/10)
- *(+854 additional chapters indexed in `Book_Lit_Master_UI_UX_Engineering.md`)*

## 📐 Distilled Engineering Rules & Actionable Patterns
### Chapter 1 [Anti-AI-Slop Dashboard Architecture]
1. **Eliminate Decorative Gradients**: AI-generated UIs paint purple-to-blue gradients on headers, buttons, and chart fills where they have nothing to say. Use **one flat semantic accent** (`indigo-600`) so color carries meaning.
2. **Drop Pastel Icon Tiles on Metric Cards**: Putting blue, green, purple, and orange icon squares on 4 KPI cards is decoration, not information. Drop the pastel tiles — **the metric number is the hero**.
3. **Break Equal-Card Monotony**: Four identical cards with the same size, weight, and green badge is "a spreadsheet with padding." Render **1 primary metric large** and **3 secondary metrics compact** so the user's eye lands once.
4. **Never Ship Database-Shaped Schemas**: Do not dump all 12 database columns onto a screen with `Delete` sitting right next to `Edit` on every row. Rank columns by user intent, limit to 1 primary CTA per view, and spec all **4 mandatory states** (*Loading sk
1. **5 Sizes Max (1.25 Modular Scale)**: Never hand-pick 11 arbitrary pixel sizes; collapse to 5 steps on a `1.25` ratio.
