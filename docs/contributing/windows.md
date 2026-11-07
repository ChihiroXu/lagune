# Windows development

## Requirements

- Windows 10 or later.
- Python 3.11 or later.
- [`uv`](https://docs.astral.sh/uv/) for the CONFLUX workspace.
- Node.js 22 or later and npm for the static website.

Use PowerShell for the commands below. From the repository root, synchronize the locked Python workspace and run its checks:

```powershell
uv sync --locked --all-packages --group dev
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
```

Set the local data root to a directory outside the repository. Create it if needed:

```powershell
$env:LAGUNE_DATA_DIR = 'D:\LaguneData'
New-Item -ItemType Directory -Force $env:LAGUNE_DATA_DIR
uv run --locked conflux data-root
```

The environment variable applies to the current PowerShell session. Configure it through your preferred local environment setup if it should persist; do not commit machine-specific paths. Data-dependent commands must report missing configuration rather than silently writing into the repository.

To develop or build the static portfolio:

```powershell
Set-Location website
npm ci
npm run dev
npm run build
```

## Spatial dependency policy

The initial CONFLUX package intentionally avoids heavyweight GIS dependencies. Add one only when a specific research need is documented and its installation is verified on Windows as well as other supported CI platforms.
