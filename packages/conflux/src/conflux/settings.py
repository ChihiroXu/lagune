"""Configuration for the local CONFLUX data boundary."""

import os
from pathlib import Path

from pydantic import BaseModel, ConfigDict


class ConfluxSettings(BaseModel):
    """Validated settings required to locate local research data."""

    model_config = ConfigDict(frozen=True)

    data_dir: Path

    @classmethod
    def from_environment(cls) -> "ConfluxSettings":
        """Load the configured data root without assuming a machine-specific path."""
        data_dir = os.environ.get("LAGUNE_DATA_DIR")
        if not data_dir:
            raise ValueError(
                "LAGUNE_DATA_DIR is not set. Configure it to a data directory "
                "outside the repository."
            )
        return cls(data_dir=Path(data_dir).expanduser())
