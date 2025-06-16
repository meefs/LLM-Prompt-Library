# Enterprise Templates

Production-grade Jinja2 templates for regulated industries and complex workflows.

## Template Suites

### Domain-Specific Kits

| Kit | Templates | Compliance Standards |
|-----|-----------|---------------------|
| **Finance** | 9 templates | Basel III/IV, FRTB, IFRS 9, MiFID II |
| **Legal** | 8 templates | GDPR, CCPA, HIPAA, SOX |
| **Medical** | 9 templates | HL7 FHIR, ICD-10, CPT, FDA |

### Functional Suites

| Suite | Purpose | Templates |
|-------|---------|-----------|
| **AI Research** | Experiment design, benchmarks | 9 templates |
| **Code Analysis** | Security, performance, refactoring | 10 templates |
| **Governance** | Policy, compliance, auditing | 9 templates |
| **Security** | Threat intel, risk assessment | 4 templates |

## Usage

> Copy any `.j2` template in this suite, fill the `params` dictionary, and send the rendered text to your LLM – zero dependencies required.

## Template Structure

All templates follow this pattern:

1. **Parameter Setup** - Extract variables from `params` object
2. **System Declaration** - Template ID and purpose  
3. **Task Definition** - Numbered steps or requirements
4. **Output Format** - Structured JSON-5 or Markdown schema

## Naming Convention

`<domain>_<function>_v<version>.j2`

Examples:
- `fin_risk_model_calibrator_v1.j2`
- `legal_contract_risk_scanner_v1.j2`
- `med_clinical_note_summarizer_v1.j2`

## Output Formats

- **JSON-5**: Structured data with comment support
- **Markdown**: Documentation and reports  
- **Unified Diff**: Code changes and patches

## Utility Macros

Each domain includes utility macros in `util_<domain>_macros.j2`:

- Text truncation functions
- Domain-specific formatters
- Validation helpers
- Common transformations

## Integration

Templates integrate with:
- CI/CD pipelines
- LangChain workflows
- Apache Airflow
- SOC automation
- Custom enterprise systems

## Standards Compliance

Templates implement:
- **Financial**: Regulatory capital calculations, stress testing
- **Legal**: Privacy impact assessments, contract analysis
- **Medical**: Clinical decision support, pharmacovigilance  
- **Security**: Threat modeling, vulnerability assessment