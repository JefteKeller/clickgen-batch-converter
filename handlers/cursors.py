import os
from typing import Iterable

from clickgen.parser import open_blob
from clickgen.writer import to_win, to_x11

from common.aliases import MakeCursorOptions


def make_static_cursor_blob(
    raw_cursor_path: str, make_cursor_options: MakeCursorOptions
):
    with open(raw_cursor_path, 'rb') as raw_cursor:
        return open_blob(
            raw_cursor.read(),
            hotspot=make_cursor_options['cursor_hotspot'],
            sizes=make_cursor_options['cursor_size'],
        )


def make_animated_cursor_blob(
    pngs: list[bytes], make_cursor_options: MakeCursorOptions
):
    return open_blob(
        pngs,
        hotspot=make_cursor_options['cursor_hotspot'],
        sizes=make_cursor_options['cursor_size'],
        delay=make_cursor_options['anim_delay'],
    )


def make_cursor_from_blob(
    cursor_name: str, cursor_blob, make_cursor_options: MakeCursorOptions
) -> None:
    output_file: str = ''
    output_dir = make_cursor_options['output_dir']

    target_platform = make_cursor_options['platform']

    match target_platform:
        case 'windows':
            ext, result = to_win(cursor_blob.frames)

            output_file = os.path.join(
                output_dir,
                f'{cursor_name}{ext}',
            )

        case 'x11':
            result = to_x11(cursor_blob.frames)

            output_file = os.path.join(
                output_dir,
                cursor_name,
            )
        case _:
            raise ValueError(f'Error: "{target_platform}" is not a valid platform.')

    os.makedirs(output_dir, exist_ok=True)

    with open(output_file, 'wb') as file:
        file.write(result)


def make_static_cursor(
    raw_cursor_files: Iterable, make_cursor_options: MakeCursorOptions
) -> None:
    for raw_cursor in raw_cursor_files:
        if raw_cursor.is_file():
            cur_blob = make_static_cursor_blob(raw_cursor.path, make_cursor_options)
            cur_name, _ = os.path.splitext(raw_cursor.name)

            make_cursor_from_blob(cur_name, cur_blob, make_cursor_options)


def make_animated_cursor(
    raw_cursor_files: Iterable, make_cursor_options: MakeCursorOptions
) -> None:
    pngs: list[bytes] = []

    raw_cursor_paths = [
        cur_files.path for cur_files in raw_cursor_files if cur_files.is_file()
    ]

    if not len(raw_cursor_paths):
        raise ValueError(
            f"""Error: There are no files in directory: "{make_cursor_options['input_dir']}"."""
        )

    for raw_cur_path in sorted((raw_cursor_paths)):
        with open(raw_cur_path, 'rb') as anim_cursor:
            pngs.append(anim_cursor.read())

    cur_blob = make_animated_cursor_blob(pngs, make_cursor_options)
    _, cur_name = os.path.split(make_cursor_options['input_dir'])

    make_cursor_from_blob(cur_name, cur_blob, make_cursor_options)


def make_cursors(make_cursor_options: MakeCursorOptions) -> None:
    with os.scandir(make_cursor_options['input_dir']) as raw_cursor_files:
        match make_cursor_options['cursor_type']:
            case 'static':
                make_static_cursor(raw_cursor_files, make_cursor_options)

            case 'animated':
                make_animated_cursor(raw_cursor_files, make_cursor_options)
