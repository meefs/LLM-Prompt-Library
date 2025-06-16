# Schema-Ops Prompting Kit

Templates for schema discovery, normalization, diffing and governance. Outputs OpenAPI/JSON-Schema artefacts for data-product pipelines.

| File | Purpose |
|------|---------|
| `sc_schema_converter_v1.j2` | Convert between Protobuf / Avro / JSON |
| `sc_schema_diff_reporter_v1.j2` | Produce breaking-change diff |
| `sc_schema_doc_generator_v1.j2` | Generate Markdown docs |
| `sc_schema_from_samples_v1.j2` | Infer schema from JSON samples |
| `sc_schema_governance_auditor_v1.j2` | Flag policy violations |
| `sc_schema_migration_planner_v1.j2` | Plan versioned migrations |
| `sc_schema_normalizer_v1.j2` | Canonicalize field names/types |
| `sc_schema_validator_v1.j2` | Validate payloads vs schema |
| `util_schema_macros.j2` | Shared helpers
