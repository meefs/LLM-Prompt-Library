# Finance Prompting Kit

Enterprise-grade Jinja2 templates that automate risk, treasury, capital and compliance workflows. Each template renders deterministic JSON-5/Markdown suitable for piping into risk engines, dashboards or CI pipelines.

| File | Purpose |
|------|---------|
| `fin_risk_model_calibrator_v1.j2` | Basel III/IV PD & LGD calibration with convergence guardrails |
| `fin_reg_capital_calc_v1.j2` | FRTB-SA capital computation & ratio impact |
| `fin_liquidity_stress_tester_v1.j2` | LCR/NSFR scenario testing & breach detection |
| `fin_pnl_reconciler_v1.j2` | SOX 404 P&L flash vs back-office reconciliation |
| `fin_trade_surveillance_v1.j2` | MiFID II real-time trade-abuse detection |
| `fin_ifrs9_impairment_engine_v1.j2` | IFRS 9 ECL calculation with overlay governance |
| `fin_alm_optimiser_v1.j2` | ALM hedge optimisation vs NII / EVE objectives |
| `fin_data_lineage_auditor_v1.j2` | COSO & BCBS 239 lineage gap analysis |
| `util_fin_macros.j2` | Shared `trunc()` macro for prompt rendering |

> Copy the `.j2` file, fill `params`, and send to your LLM – zero external dependencies required.
