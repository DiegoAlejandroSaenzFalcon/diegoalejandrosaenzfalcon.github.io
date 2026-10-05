# Governance — Diego Alejandro Saenz Falcon Portfolio

## Overview
This portfolio is a **public presentation surface** for Diego Alejandro Saenz Falcon's professional profile. It is **not** the source of truth for governance, security policies, or operational directives.

## Central Governance Authority
**Directivas-de-Seguridad** (private repository) is the single source of truth for:
- Security policies
- Operational directives
- Agent rules and workflows
- Compliance requirements
- Risk management frameworks

This portfolio **consumes and represents** public information derived from that authority. It does not define, duplicate, or override any private policy.

## Portfolio Responsibilities
- Present professional CV, experience, education, certifications, and projects accurately
- Maintain link integrity and HTML validity
- Enforce public-facing security basics (no secrets, valid HTTPS links, CSP-ready structure)
- Surface governance references transparently without exposing private content
- Pass CI checks: secret scan, HTML validation, link check, required file presence

## What This Repository Does NOT Do
- Store or define security policies
- Host private governance documents
- Declare VERIFIED status without authoritative source
- Modify professional data without explicit authorization
- Create parallel governance structures
- Mutate the default branch automatically from CI

## Change Control
All modifications to this repository follow the rules in AGENTS.md:
1. Feature branch + Pull Request required
2. No direct pushes to main
3. Conventional commit messages
4. CI must pass before merge consideration
5. Final authority (Diego Alejandro Saenz Falcon) merges

## CI Control
The repository CI is **validation-only**. CI may inspect, test and report repository state, but it must not modify tracked source files, create commits, or push to the default branch. Source changes are made through an authorized branch and Pull Request.

The CI architecture and failure-prevention rules are documented in `CI-POLICY.md`.

## Compliance
This portfolio aligns with the governance framework defined in Directivas-de-Seguridad. Compliance is verified through:
- Automated CI checks (secrets, HTML, links, structure)
- Manual review by final authority
- No public disclosure of private policy content
- No CI-driven source mutation

## Contact
Governance inquiries: diegoalejandrosaenzfalcon@gmail.com (subject: [GOVERNANCE] Portfolio)
