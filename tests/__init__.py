from pathlib import Path


def get_assets_path(extension: str) -> list[str]:
    return [file.as_posix() for file in Path('assets').glob(f'*.{extension}')]
