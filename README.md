# LAGUNE

**Spatial Intelligence & Research**

LAGUNE is a research platform for investigating spatial questions and communicating evidence through maps and other visual forms. It is organized as a modular monorepo so research, spatial computation, design standards, and public publishing can evolve together without becoming one coupled application.

## Platform

- **CONFLUX** — spatial intelligence engine for reproducible spatial analysis.
- **INSIGHTS** — research and knowledge library for questions, methods, sources, outputs, and provenance.
- **DESIGN** — visual language, cartographic standards, and visualization standards.
- **WEBSITE** — public portfolio for selected research and its communication.

LAGUNE prioritizes transparent methods, documented sources, and contextual interpretation. It is a research platform, not a general-purpose AI product. Its initial foundation does not include an autonomous agent runtime, backend services, or a database.

## Repository map

```text
packages/conflux/       Python spatial-engine package
insights/               Research records and metadata
design/                 Brand and visualization standards
website/                Static research portfolio
docs/architecture/      System boundaries, data lifecycle, and decisions
docs/contributing/      Development environment guidance
```

See [System context](docs/architecture/system-context.md) and [Data lifecycle](docs/architecture/data-lifecycle.md) for the architecture and data-handling conventions.

## Project status

**Stage A — Complete:** repository foundation, platform identity, architecture and data-boundary documentation, and Windows development guidance.

**Stage B — Planned, not yet accepted:** finalize and review the CONFLUX, INSIGHTS, and DESIGN foundations and Copilot customization. Early scaffold files for these areas are present in the worktree.

**Stage C — Planned, not yet accepted:** finalize and review the minimal static Astro portfolio and cross-platform CI. Early scaffold files are present in the worktree.

## Data handling

Large raw datasets and generated spatial outputs belong outside Git under `LAGUNE_DATA_DIR`; see the [data lifecycle](docs/architecture/data-lifecycle.md) for the recommended layout. Only small synthetic or explicitly authorized redistributable fixtures in `packages/conflux/tests/fixtures/` may be committed. Private, confidential, non-redistributable, and sensitive research data are prohibited.

## Development

- [Windows development setup](docs/contributing/windows.md)
- [CONFLUX package setup](packages/conflux/README.md)

Use `uv` for Python dependency management. Generate and update `uv.lock` through dependency resolution; do not edit the lockfile by hand.
