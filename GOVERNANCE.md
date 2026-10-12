# Governance — Diego Alejandro Saenz Falcon Portfolio

## Overview
This portfolio is a public presentation surface for Diego Alejandro Saenz Falcon's professional profile. It is not the source of truth for governance, security policies, or operational directives.

## Central Governance Authority
**Directivas-de-Seguridad** (private repository) is the single source of truth for security policies, operational directives, agent rules, compliance requirements and risk management frameworks.

## Portfolio Responsibilities
- Present professional experience, education, certifications and projects accurately.
- Maintain link integrity and HTML validity.
- Enforce public-facing security basics and avoid exposing private content.
- Pass CI checks for secrets, HTML structure and required governance files.

## What This Repository Does NOT Do
- Store or define security policies.
- Host private governance documents.
- Declare VERIFIED status without authoritative evidence.
- Modify professional data without explicit authorization.
- Create parallel governance structures.
- Mutate the default branch automatically from CI.

## Change Control
1. Feature branch and Pull Request required.
2. No direct pushes to main.
3. Conventional commit messages.
4. CI must pass before merge consideration.
5. Diego Alejandro Saenz Falcon retains final merge authority.

## CI Control
CI is validation-only. It may inspect, test and report repository state, but must not modify tracked source files, create commits or push to the default branch.
