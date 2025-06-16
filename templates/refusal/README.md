# Refusal & Safe-Completion Kit

Templates that enforce policy-aligned refusals, partial comply, rate limits and escalation paths.

| File | Purpose |
|------|---------|
| `rs_audit_logger_v1.j2` | Log refusals & policy events |
| `rs_escalation_router_v1.j2` | Escalate complex requests to humans |
| `rs_multilang_refusal_v1.j2` | Localised refusal generator |
| `rs_partial_comply_redactor_v1.j2` | Redact sensitive output & comply |
| `rs_policy_pivot_sugg_v1.j2` | Suggest policy pivot options |
| `rs_rate_limit_handler_v1.j2` | Graceful over-quota messages |
| `rs_refusal_gate_v1.j2` | Main policy refusal logic |
| `rs_soft_refusal_builder_v1.j2` | Offer safe alternatives |
| `util_refusal_macros.j2` | Shared helpers
