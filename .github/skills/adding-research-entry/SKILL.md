---
name: adding-research-entry
description: Create or update an INSIGHTS research metadata record that follows the LAGUNE YAML schema and data-handling rules.
---

# Adding a research entry

1. Read `insights/README.md` and `insights/schema/research-record.schema.yaml`.
2. Assign a unique `research_id`; do not reuse an existing ID.
3. Record the title, category, status, methods, data sources, outputs, and provenance required by the schema.
4. Include source citations, access dates, and known license or usage information. Do not invent missing details; mark gaps for follow-up in notes.
5. Refer to large files by stable URI or path relative to `LAGUNE_DATA_DIR`; never place bulk data or generated outputs in the repository.
6. Use only synthetic or redistributable examples in tests and documentation.
7. Review the completed YAML against the schema and confirm that the record contains no machine-specific absolute paths or sensitive information.
