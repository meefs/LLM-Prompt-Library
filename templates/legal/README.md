# Legal Prompting Kit

Eight Jinja2 templates that transform an LLM into a contracts counsel, compliance analyst, e-discovery tuner, privacy officer, case-law summarizer, policy drafter & citation checker.

| File | Purpose |
|------|---------|
| `legal_contract_risk_scanner_v1.j2` | Clause-level risk scoring & redlines |
| `legal_clause_library_builder_v1.j2` | Build playbook clause library from corpora |
| `legal_reg_compliance_mapper_v1.j2` | Map obligations across GDPR/CCPA/HIPAA/SOX |
| `legal_ediscovery_prioritizer_v1.j2` | Rank documents by relevance × cost (Sedona) |
| `legal_privacy_impact_assessor_v1.j2` | ISO 27701 / GDPR PIA risk assessment |
| `legal_case_law_summarizer_v1.j2` | IRAC summary with key cites |
| `legal_policy_drafter_v1.j2` | Draft internal policies aligned with ISO & law |
| `legal_stat_citation_validator_v1.j2` | Validate Bluebook/ALWD statutory citations |
| `util_legal_macros.j2` | Shared `trunc()` macro |

> Copy the `.j2` file, fill `params`, and send to your LLM – zero external dependencies required.
