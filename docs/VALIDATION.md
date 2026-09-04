# Validation Approach

LabOS separates AI scientific decisions from exact molecular calculations.

## Main validation principles

- Exact sequence operations are delegated to deterministic scientific software.
- Material/source identity is tracked across workflows.
- Missing required evidence produces warnings or blocks rather than invented molecular data.
- Scientific evidence from different engines can be retained separately rather than collapsed into an unsupported score.
- Construct-validation depth can increase when PCR history or construct complexity warrants it.

## Automated checks

The private project uses pytest and GitHub Actions for backend, routing, architecture and scientific regression tests, together with frontend production-build checks.

Software validation is not a substitute for experimental validation.
