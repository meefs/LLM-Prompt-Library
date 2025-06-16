# Medical Prompting Kit

Eight Jinja2 templates for clinical documentation, coding, lab/rad interpretation, prior auth, FHIR validation & pharmacovigilance — HIPAA-aware and standards aligned.

| File | Purpose |
|------|---------|
| `med_clinical_note_summarizer_v1.j2` | APSO/SOAP summaries with PHI scrub |
| `med_icd10_cpt_coder_v1.j2` | Auto-code ICD-10 & CPT 2025 |
| `med_drug_interaction_checker_v1.j2` | Check DrugBank/FDA interactions |
| `med_lab_result_interpreter_v1.j2` | Interpret labs vs age/sex ranges |
| `med_radiology_report_generator_v1.j2` | Structured ACR style report |
| `med_prior_authorization_drafter_v1.j2` | Draft payer PA letters |
| `med_fhir_bundle_validator_v1.j2` | Validate HL7 FHIR bundles |
| `med_adverse_event_detector_v1.j2` | Detect adverse events & build E2B |
| `util_med_macros.j2` | Shared macro |

> Copy the `.j2` file, fill `params`, and send to your LLM – zero external dependencies required.
