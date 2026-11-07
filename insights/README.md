# INSIGHTS

INSIGHTS is LAGUNE's research and knowledge library. It keeps structured research metadata and provenance in Git while leaving large datasets and generated outputs outside the repository.

Each research record is YAML and follows [`schema/research-record.schema.yaml`](schema/research-record.schema.yaml). The schema requires a research ID, title, category, status, methods, data sources, outputs, and provenance. [`research/example.yml`](research/example.yml) demonstrates the record shape using synthetic example content.

Use stable, unique research IDs. Cite sources and record access dates and applicable usage restrictions. Output references should identify files or locations under the configured `LAGUNE_DATA_DIR` without embedding machine-specific absolute paths. Do not commit private, restricted, or bulk source data.
