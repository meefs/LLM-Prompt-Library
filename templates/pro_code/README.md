# Pro-Code Prompting Kit

Templates that turn an LLM into a senior software-engineer: debugging, refactoring, migration design, security reviews and more. All emit structured JSON-5/Markdown for CI pipelines.

| File | Purpose |
|------|---------|
| `code_bug_explainer_v1.j2` | Root-cause analysis & remediation hints |
| `code_db_migration_designer_v1.j2` | Generate SQL/DDL migration plans |
| `code_iac_guardrail_v1.j2` | Scan IaC for CIS policy violations |
| `code_perf_profiler_v1.j2` | Identify hotspots & perf budget breaches |
| `code_refactor_planner_v1.j2` | Refactor roadmap with diff chunks |
| `code_security_auditor_v1.j2` | OWASP-style security checklist |
| `code_spec_normalizer_v1.j2` | Normalize spec docs to OpenAPI/ADR |
| `code_unit_test_writer_v1.j2` | Auto-generate parametric unit tests |
| `util_code_macros.j2` | Shared helpers |

> Copy the `.j2` file, fill `params`, and send to your LLM – zero external dependencies required.
