# Point-of-Care Clinical Prompting Kit

Triage, antimicrobial stewardship, dosing, imaging appropriateness and discharge instructions for frontline care teams.

| File | Purpose |
|------|---------|
| `pc_triage_urgency_scorer_v1.j2` | Compute ESI & NEWS-2 urgency scores |
| `pc_differential_to_workup_v1.j2` | Map DDx list to evidence-based work-up |
| `pc_antibiotic_steward_v1.j2` | Select empiric antibiotics & de-escalation |
| `pc_weight_based_dose_calc_v1.j2` | Safe kg-based dosing w/ renal adjust |
| `pc_polypharmacy_beers_checker_v1.j2` | Flag BEERS-listed meds |
| `pc_imaging_appropriateness_v1.j2` | Score imaging vs ACR criteria |
| `pc_chronic_care_plan_builder_v1.j2` | Build SMART goals & follow-up |
| `pc_discharge_instruction_writer_v1.j2` | Write 6th-grade discharge instructions |
| `util_pc_macros.j2` | Shared macro |

> Copy the `.j2` file, fill `params`, and send to your LLM – zero external dependencies required.
