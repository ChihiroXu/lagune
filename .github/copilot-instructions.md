# LAGUNE project instructions

## Project purpose and structure

LAGUNE is a Spatial Intelligence & Research platform, not a generic AI startup. Keep work within the modular boundaries documented in `docs/architecture/system-context.md`:

- CONFLUX: spatial computation and reproducible analysis.
- INSIGHTS: research metadata, sources, methods, outputs, and provenance.
- DESIGN: identity, tokens, cartographic standards, and visualization standards.
- WEBSITE: static public presentation of selected research.

## Engineering and data practices

- Read relevant architecture and module documentation before changing boundaries or formats.
- Keep large datasets and generated outputs outside Git under `LAGUNE_DATA_DIR`. Never add real or sensitive data as fixtures; use small synthetic fixtures only.
- Do not silently fall back to repository-local or machine-specific data paths when `LAGUNE_DATA_DIR` is missing.
- Keep CONFLUX lightweight; add spatial libraries only for a documented need and a Windows-compatible installation path.
- Use `uv` for Python workspace dependency management. Update `uv.lock` through `uv lock`; do not hand-edit the lockfile.
- Keep runtime dependencies in `packages/conflux/pyproject.toml` and shared development tools in the root `pyproject.toml`.
- Preserve Windows compatibility. Use PowerShell examples in Windows instructions and avoid hard-coded user-specific paths.
- Keep the website static. Backend services, databases, authentication, and AI interfaces are out of scope.
- Do not implement an autonomous AI agent runtime as part of the current foundation.

## Quality

Add focused tests for new behavior and run the relevant checks in `.github/workflows/ci.yml`. Document data sources, methods, provenance, and limitations; distinguish research evidence from interpretation.
