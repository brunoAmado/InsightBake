@setmiddle_tenant @dev_latest_modules @ux_engine_2_8 @no_feature_placeholders
Feature: InsightBake Reverse-Engineered Contract, Live DEV Module Resolution & Anti-AI-Slop UI Certification
  As the SetMiddle Dev Team (setmiddle-dev-team)
  I want InsightBake (InsightBake™ — Arrhenius Fermentation, Baker's % Scaling & Bi-Temporal HACCP) certified with BDD scenarios and zero feature placeholders
  So that every backend endpoint and frontend control works as expected in DEV and CI

  Background:
    Given the client tenant is "SETMIDDLE" and the active team is "setmiddle-dev-team"
    And the environment profile is "DEV" resolving shared modules from "LATEST-HEAD"

  Scenario: 1. Backend health and primary domain action execute with zero feature placeholders
    When the SetMiddle Dev Team calls GET "/api/bake/status" or invokes "/api/bake/execute" on port 4030
    Then the service responds with deterministic domain output and zero unimplemented stubs

  Scenario: 2. Frontend Web Component enforces persistent labels, input placeholders, and 4-state UX
    Given the "<insightbake>" component is rendered
    Then every input control has an explicit "<label for=...>" above it and a descriptive "placeholder" attribute inside the input box
    And submitting the form triggers "/api/bake/execute" with loading skeleton, aria-live status, and inline retry support
