"""Command-line entry point for CONFLUX."""

import typer

from conflux.settings import ConfluxSettings

app = typer.Typer(no_args_is_help=True, help="Lightweight tools for LAGUNE spatial research.")


@app.callback()
def main() -> None:
    """Run CONFLUX diagnostics and spatial research tools."""


@app.command("data-root")
def data_root() -> None:
    """Print the configured local data root."""
    try:
        settings = ConfluxSettings.from_environment()
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error
    typer.echo(settings.data_dir)
