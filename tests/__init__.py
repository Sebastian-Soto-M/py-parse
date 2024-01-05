from pathlib import Path


def get_assets_path(extension: str) -> dict[str, str]:
    files = {file.stem: file.as_posix()
             for file in Path('assets').glob(f'*.{extension}')}
    return files
