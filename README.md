# LLM Prompt Library

[![GitHub stars](https://img.shields.io/github/stars/abilzerian/LLM-Prompt-Library?style=for-the-badge)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/abilzerian/LLM-Prompt-Library?style=for-the-badge)](../../network/members)
[![Issues](https://img.shields.io/github/issues/abilzerian/LLM-Prompt-Library?style=for-the-badge)](../../issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-informational?style=for-the-badge)](LICENSE)

> **Experimental prompt templates for every major LLM.**

A constantly evolving library of prompts & templates I've been tinkering with since Dec. 2022.

## Quick Start

```bash
git clone https://github.com/abilzerian/LLM-Prompt-Library.git
cd LLM-Prompt-Library

# Browse community prompts
ls prompts/

# Use enterprise templates  
ls templates/
```

## What's Inside

### Enterprise-style Templates (`templates/`)
**164 experimental Jinja2 templates**:

| Suite | Purpose | Standards Goal |
|-------|---------|-----------|
| **Finance** | Risk, capital, liquidity | Basel III/IV, FRTB, IFRS 9 |
| **Private Equity** | LBO models, ESG tracking, waterfalls | ILPA DDQ 2024, IFRS 13 |
| **Venture Capital** | Fund reporting, carry, cash-flow forecasting | ILPA Reporting 3.0 |
| **Legal** | Contract analysis, privacy impact | GDPR, CCPA, HIPAA |
| **Medical** | Clinical decision support, FHIR validation | HL7 FHIR, ICD-10 |
| **Pro Code** | Code review, bug explanation, refactoring | OWASP ASVS |
| **AI Research** | Benchmarking, experiment design | Statistical rigor |
| **Governance** | Policy compliance, risk assessment | SOX, COSO |

### Community Prompts (`prompts/`)
**60+ curated prompts** organized by domain:

| Category | Count | Examples |
|----------|-------|----------|
| Programming | 17 | Python, AWS, Code Review |
| Writing | 14 | Proofreading, Summarization |
| Miscellaneous | 8 | Red-teaming, Adventures |
| Meta | 7 | Prompt engineering, DALL-E |
| Finance | 3 | 10-K Analysis, VC |
| Medical | 5 | Clinical trials, diagnostics |
| Legal | 2 | Case law, contracts |
| Marketing | 2 | Ad copy, social media |
| Sales | 1 | Email drafting |
| Creative | 2 | Storytelling, dialogue |

## Usage

Copy any `.j2` template that fits your need, fill in the `params` values (or edit the inline `{{ placeholders }}`), then send the rendered prompt to your LLM.  
No external Python libraries or template loaders are required.

⸻

## Community & Stats

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=abilzerian/LLM-Prompt-Library&type=Date&theme=dark">
    <img alt="Star history" src="https://api.star-history.com/svg?repos=abilzerian/LLM-Prompt-Library&type=Date">
  </picture>
</p>

---

<div align="center">
  <sub>© 2025 | Created by <a href="https://x.com/alexbilz">Alex Bilzerian</a></sub>
</div>
