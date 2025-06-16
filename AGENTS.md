# Agent Guide

> Simple handbook for **autonomous AI agents** contributing to this repository.

## Mission

Maintain a **high-quality prompt and template library** that's easy to use and understand.

## Repository Structure

| Path | Purpose |
|------|---------|
| `prompts/` | Community prompt collection (60+ prompts) |
| `templates/` | Enterprise Jinja2 templates (200+ templates) |

## Simple Workflow

1. **Fork** the repository
2. **Add/Edit** prompts or templates
3. **Follow** existing format patterns
4. **Submit** pull request

## Prompt Guidelines

### File Structure
- Location: `prompts/<category>/<Name>.md`
- Format: Standard markdown
- Style: Clear, actionable instructions
- Size: Keep concise and focused

### Required Sections
1. Title (H1)
2. Purpose description
3. Instructions in code block
4. Example usage (optional)

### Template Guidelines

### Jinja2 Templates
- Location: `templates/<category>/<name>_v<version>.j2`
- Standards: Domain-specific compliance when applicable
- Output: Structured JSON-5 or Markdown
- Macros: Use utility files for reusable functions

## Quality Standards

- **Clear and actionable** - Instructions should be unambiguous
- **Safe content** - No harmful or malicious prompts
- **Proper formatting** - Follow existing patterns
- **Relevant examples** - Include usage demonstrations when helpful

## Contributing Types

### New Prompts
1. Choose appropriate category in `prompts/`
2. Create descriptive filename
3. Follow standard format
4. Test with multiple LLMs if possible

### New Templates  
1. Select correct domain in `templates/`
2. Follow naming convention
3. Include proper documentation
4. Test rendering with sample data

### Improvements
- Fix formatting issues
- Update outdated information  
- Add missing examples
- Improve clarity

---

Keep it simple. Focus on quality. Help the community. ✨