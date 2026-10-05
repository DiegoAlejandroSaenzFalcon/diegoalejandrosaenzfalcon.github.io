# CI Policy — GitHub Pages Portfolio

## Purpose

This document defines the continuous-integration contract for the public portfolio repository. CI exists to validate proposed repository state before merge; it is not an authoring or deployment agent.

## Authority

The repository follows the central authority defined by `Directivas-de-Seguridad` and the local rules in `AGENTS.md`, `SECURITY.md`, and `GOVERNANCE.md`.

## Mandatory CI properties

1. **Validation only:** workflows may inspect, scan and test; they must not modify tracked source files.
2. **No automatic commits:** CI must never create commits as part of validation.
3. **No automatic pushes:** CI must never push to `main` or any other branch.
4. **Pull-request first:** proposed changes are validated on the feature branch through the Pull Request.
5. **Fail closed:** a failed validation blocks merge consideration; it is not repaired automatically by mutating repository content.
6. **Reproducibility:** the same source revision must produce deterministic validation results as far as the external services used by the checks permit.
7. **Least privilege:** workflow permissions remain read-only unless a separately justified workflow contract explicitly requires another permission.
8. **Evidence before success:** a green run is evidence that the defined checks passed for that revision; it is not permission to merge by itself.

## Failure-prevention process

Before pushing a change:

1. Audit the governing contracts and applicable Markdown instructions.
2. Validate the changed files locally.
3. Run the relevant static checks and tests.
4. Review the diff for scope, truthfulness and security.
5. Commit once the local gate is clean.
6. Push the authorized branch.
7. Inspect the resulting GitHub Actions run.
8. If CI fails, diagnose the actual failing step and fix the source on the feature branch; never add automation whose purpose is to rewrite the repository until CI becomes green.

## Historical failure handling

A historical failed run is not erased or rewritten. It remains part of the repository's audit history. The objective is to prevent new failures caused by avoidable workflow design defects and to document the root cause when a failure occurs.

## Current known root cause addressed

An earlier Governance CI run failed because a case-sensitive text assertion did not match the capitalization used by `GOVERNANCE.md`. The assertion was corrected to be case-insensitive in commit `8fd5a27`. The following Governance CI run completed successfully.

A separate historical workflow, `apply-final-corrections.yml`, was identified as non-compliant because it could modify `index.html`, commit, and push changes automatically. It is removed by this integration so CI cannot repair source state by mutation.

## Definition of done for CI changes

A CI change is complete only when:
- workflow files comply with this policy;
- applicable repository contracts and Markdown instructions have been reviewed;
- local validation passes;
- the Pull Request CI run is green;
- no workflow performs unauthorized source mutation;
- the resulting state is documented.
