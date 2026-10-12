# CI Policy — GitHub Pages Portfolio

## Purpose
CI validates proposed repository state before merge; it is not an authoring or deployment agent.

## Mandatory properties
1. Validation only: workflows may inspect, scan and test, but must not modify tracked source files.
2. No automatic commits or pushes.
3. Pull-request-first change control.
4. Fail closed: failed validation is diagnosed and fixed on the feature branch.
5. Least privilege: read-only workflow permissions unless separately justified.
6. Evidence before success: a green run validates only the checks defined for that revision.

## Failure-prevention process
1. Review governing contracts and Markdown instructions.
2. Validate changed files locally.
3. Run static checks and tests. Secret scanning on Pull Requests requires full Git history (checkout fetch-depth: 0).
4. Review the diff for scope, truthfulness and security.
5. Commit on the authorized branch.
6. Inspect GitHub Actions results.
7. Diagnose actual failures; never create a workflow that rewrites source until CI becomes green.

## Definition of done
- CI workflows comply with this policy.
- Content and links are reviewed.
- Pull Request CI passes.
- No workflow performs unauthorized source mutation.
- The final state is documented.
