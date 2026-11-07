# Data lifecycle and storage

## Storage boundary

Large source datasets, intermediate files, and generated outputs must remain outside the Git working tree. Set `LAGUNE_DATA_DIR` to an absolute path on an appropriate local or managed storage volume, for example:

```powershell
$env:LAGUNE_DATA_DIR = 'D:\LaguneData'
```

The value above is an example, not a required location. Do not commit machine-specific paths or data. If `LAGUNE_DATA_DIR` is unset, data-dependent workflows should report the missing configuration rather than silently writing into the repository.

## Recommended layout

```text
<LAGUNE_DATA_DIR>/
  raw/          Original inputs; preserve source files
  interim/      Re-creatable processing intermediates
  processed/    Analysis-ready datasets
  outputs/      Maps, tables, and other generated deliverables
```

Keep the research catalog in INSIGHTS limited to metadata and references; it should not embed bulk spatial data. Record source attribution, acquisition details, applicable licenses or restrictions, transformations, and links between research records and generated outputs.

## Git policy

- Large raw datasets and generated spatial outputs belong outside Git under `LAGUNE_DATA_DIR`.
- Only small synthetic or explicitly authorized redistributable test fixtures in `packages/conflux/tests/fixtures/` may be committed.
- Private, confidential, non-redistributable, and sensitive research data are prohibited from Git, including fixtures.
- Keep root `/data/`, `packages/conflux/data/`, and nested `local-data/`, `private-data/`, `processed-data/`, and `outputs/` directories ignored as a safety net; this does not replace storing large data outside the repository.
- Do not commit credentials, caches, or generated deliverables.
- Do not add blanket ignore rules for common spatial file extensions; allowed fixture files belong only in the explicit test-fixtures directory above.

## Reproducibility

Research records should identify the data sources, methods, and outputs involved. Analysis code should not assume a developer-specific drive or absolute path; data-dependent commands should obtain their root from `LAGUNE_DATA_DIR` and make missing configuration explicit.
