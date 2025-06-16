# Venture-Capital Term-Sheet Suite

Eight Jinja2-ready templates that span the venture financing lifecycle—seed SAFEs through late-stage preferred equity.

| Template | Purpose | Standards |
|----------|---------|-----------|
| `vc_seed_safe_generator_v1.j2` | Generate YC Post-Money SAFE boilerplate | YC SAFE 2023 |
| `vc_seriesA_pref_sheet_builder_v1.j2` | Draft NVCA Series-A term sheet | NVCA Model 2024 |
| `vc_term_sheet_comparator_v1.j2` | Diff two term sheets with materiality heat-map | Aumni Benchmarks 2024 |
| `vc_liquidation_waterfall_sim_v1.j2` | Simulate distribution waterfall | NVCA / Model Docs |
| `vc_antidilution_calculator_v1.j2` | Compute price-based anti-dilution resets | Oxford Seed Docs 2025 |
| `vc_option_pool_shuffle_analyzer_v1.j2` | Quantify dilution from option-pool shuffle | Carta Study 2024 |
| `vc_redline_negotiation_writer_v1.j2` | Produce red-line diff for counsel | DocuSign diff workflows |
| `vc_postmoney_cap_table_scenarios_v1.j2` | Project dilution across future rounds | Standard cap-table math |
| `vcf_fund_perf_dashboard_v1.j2` | Compute fund-level TVPI/DPI/IRR dashboard | ILPA 3.0, GIPS |
| `vcf_lp_quarterly_report_builder_v1.j2` | Generate ILPA-compliant LP report | ILPA 3.0 |
| `vcf_carry_waterfall_calc_v1.j2` | Calculate LP/GP distributions | Fund LPA specs |
| `vcf_cashflow_forecast_engine_v1.j2` | Forecast capital calls and dists | Treasury models |
| `vcf_secondaries_pricing_model_v1.j2` | Price fund interests in secondaries | IHS Markit 2024 |
| `vcf_spv_admin_packet_v1.j2` | Produce SPV admin & K-1 packet | AICPA standards |
| `vcf_esg_lp_disclosure_builder_v1.j2` | Build ESG/DEI disclosures | UN PRI, ILPA ESG |
| `vcf_adv_part2_filer_v1.j2` | Draft SEC Form ADV Part 2 brochure | SEC ADV Part 2 |

## Usage Snippet
> Copy the `.j2` file, fill `params`, and send to your LLM – zero external dependencies required.

## Governance Triggers
See top-level documentation for deal-guardrails mapping (IC approvals, counsel review, etc.).
