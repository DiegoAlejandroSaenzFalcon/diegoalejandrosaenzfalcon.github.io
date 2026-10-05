# AGENTS.md — Portfolio Governance Instructions

## Authority
- **Final authority**: Diego Alejandro Saenz Falcon
- **Central policy authority**: Directivas-de-Seguridad (private repository)
- This portfolio is a **public presentation surface**, not the source of truth for governance.

## Agent Rules
1. **Read before acting**: Every agent must read AGENTS.md, SECURITY.md, GOVERNANCE.md, and llms.txt before making changes.
2. **Branch + PR only**: All changes must be made via feature branch and Pull Request against `main`. No direct pushes to `main`.
3. **No secrets**: Never commit secrets, keys, tokens, or sensitive data.
4. **No invented content**: Do not fabricate professional data, CV content, or declare anything as "VERIFIED" without authoritative source.
5. **Preserve professional data**: Do not modify CV, experience, education, contact, or design except to fix links/integrity.
6. **Governance reference only**: This repo consumes/represents public information; the source of truth for governance remains Directivas-de-Seguridad.
7. **Minimal changes**: Implement only what is required for governance, security, and integrity.

## Workflow
- Create feature branch → implement changes → commit with conventional message → push → open PR → **do not merge** (authority merges).
- CI must pass: secret scan, HTML validation, link check (with private link handling), required file validation.