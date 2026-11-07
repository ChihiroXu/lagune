# CONFLUX

CONFLUX is LAGUNE's lightweight Python foundation for reproducible spatial research. Its initial package provides validated configuration and a small CLI diagnostic; it does not include heavyweight GIS libraries or an AI agent runtime.

The package reads `LAGUNE_DATA_DIR` as the root for local datasets and generated outputs. It does not create that directory or copy data into the repository.

From the repository root, install the workspace and shared development tools with:

```powershell
uv sync --all-packages --group dev
uv run conflux data-root
```

The CLI reports a clear error if `LAGUNE_DATA_DIR` is not set. Package-specific runtime dependencies are declared here; shared test and lint tools are declared in the root `pyproject.toml`.
