"""Collect only documented Python modules and objects for MkDocs."""

import ast
from pathlib import Path


def source_files(config):
    root = Path(config.config_file_path).resolve().parent
    excluded = {
        Path(config.docs_dir).resolve(),
        Path(config.site_dir).resolve(),
        root / "site",
    }
    for directory, folders, filenames in root.walk():
        folders[:] = sorted(
            name for name in folders
            if not name.startswith(".")
            and name not in {"__pycache__", "venv", "node_modules"}
            and directory / name not in excluded
        )
        for filename in sorted(filenames):
            source = directory / filename
            if source.suffix != ".py" or source == Path(__file__).resolve():
                continue
            relative = source.relative_to(root)
            if relative == Path("__init__.py"):
                continue
            yield relative


def on_config(config):
    """Watch every source directory while serving the documentation."""
    root = Path(config.config_file_path).resolve().parent
    watched = {str(root / source.parts[0]) for source in source_files(config)}
    config.watch.extend(sorted(watched - set(config.watch)))
    return config


def on_page_markdown(markdown, page, config, **kwargs):
    """Expand the reference marker on every build, including newly added files."""
    if page.file.src_uri != "references.md":
        return markdown

    root = Path(config.config_file_path).resolve().parent
    sections = []
    current_folder = None
    for source in source_files(config):
        tree = ast.parse((root / source).read_text(encoding="utf-8-sig"))
        if not any(
            ast.get_docstring(node)
            for node in ast.walk(tree)
            if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
        ):
            continue
        if source.parent != current_folder:
            current_folder = source.parent
            sections.append(f"## {current_folder.as_posix()}\n")
        parts = source.with_suffix("").parts
        if parts[-1] == "__init__":
            parts = parts[:-1]
        identifier = ".".join(parts)
        sections.append(f"### {source.name}\n\n::: {identifier}\n")

    return markdown.replace("<!-- auto-reference -->", "\n".join(sections))
