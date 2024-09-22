from pathlib import Path
from typing import Union
import bpy


def path_resolve(path: Union[str, Path]) -> Path:
    if isinstance(path, str):
        return Path(bpy.path.abspath(path))
    elif isinstance(path, Path):
        return Path(bpy.path.abspath(str(path)))
    else:
        raise ValueError(f"Unable to resolve path: {path}")


def active_object(context: bpy.types.Context = None) -> bpy.types.Object:
    if context is None:
        return bpy.context.active_object

    return context.active_object
