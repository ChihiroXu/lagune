# ADR 0002: Keep large data and generated outputs outside Git

- **Status:** Accepted
- **Date:** 2026-11-07

## Context

Spatial datasets and generated deliverables can be large, sensitive, restricted, or reproducible from documented sources and methods. Committing them would make repository size and data access difficult to manage.

## Decision

Keep large raw datasets and generated spatial outputs outside Git, rooted at the developer-configured `LAGUNE_DATA_DIR`. Track research metadata and provenance in the repository instead. Only small synthetic or explicitly authorized redistributable test fixtures in `packages/conflux/tests/fixtures/` may be committed. Private, confidential, non-redistributable, and sensitive research data are prohibited.

## Consequences

- Data-dependent workflows must obtain the configured data root and explain missing configuration.
- Research metadata must describe sources and outputs without embedding bulk files.
- Git ignore rules are a local safety net, not a substitute for storing data outside the repository.
- Test fixtures remain reviewable and portable across Windows and other supported environments.
