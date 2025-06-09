import os
from typing import TypedDict


class MakeCursorOptions(TypedDict):
    input_dir: os.PathLike
    output_dir: os.PathLike
    platform: str
    cursor_type: str
    cursor_size: list[int]
    cursor_hotspot: tuple[int, int]
    anim_delay: int | None
