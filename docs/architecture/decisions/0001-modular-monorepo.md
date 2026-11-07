# ADR 0001: Use a modular monorepo

- **Status:** Accepted
- **Date:** 2026-11-07

## Context

LAGUNE combines spatial computation, research curation, visual standards, and public communication. These concerns need distinct boundaries, while shared documentation and coordinated changes benefit from a single repository.

## Decision

Use one repository with separate top-level areas for CONFLUX, INSIGHTS, DESIGN, and WEBSITE, supported by shared architecture documentation. Keep module-specific dependencies and implementation details within their owning areas.

## Consequences

- A contributor can discover platform-level architecture and conventions in one place.
- Each module can evolve independently within its documented responsibility.
- CI must validate relevant components without making optional modules or large datasets prerequisites for unrelated work.
- The monorepo is not a mandate to couple module internals or introduce a central runtime.
