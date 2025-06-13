import argparse

from pathvalidate.argparse import sanitize_filepath_arg

from common.aliases import MakeCursorOptions


def get_cmd_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i',
        '--input-dir',
        type=sanitize_filepath_arg,
        required=True,
        help='Path to a directory with cursor files in PNG format.',
    )

    parser.add_argument(
        '-o',
        '--output-dir',
        type=sanitize_filepath_arg,
        required=True,
        help='Output directory for the cursor files.',
    )

    parser.add_argument(
        '-p',
        '--platform',
        type=str,
        required=True,
        choices=['windows', 'x11'],
        help='Target system platform.',
    )

    parser.add_argument(
        '-t',
        '--cursor-type',
        type=str,
        required=True,
        choices=['static', 'animated'],
        help='Cursor type.',
    )

    parser.add_argument(
        '-s',
        '--cursor-size',
        type=str,
        nargs=1,
        default=32,
        help='Cursor size. The following pattern can be used to enable canvasing: "size:canvas_size". Default: %(default)s',
    )

    parser.add_argument(
        '-x',
        '--hotspot-x',
        type=int,
        default=5,
        help='Hotspot value to be used in the X axis. Default: "%(default)s"',
    )

    parser.add_argument(
        '-y',
        '--hotspot-y',
        type=int,
        default=5,
        help='Hotspot value to be used in the Y axis. Default: "%(default)s"',
    )

    parser.add_argument(
        '-d',
        '--anim-delay',
        type=int,
        default=1,
        help='Animation delay to be used for animated cursors. Default: "%(default)s"',
    )

    return parser.parse_args()


def success_message(make_cursor_options: MakeCursorOptions) -> str:
    return f"""
    Operation completed using the following settings:

    Platform: {make_cursor_options['platform']}
    Input Directory: {make_cursor_options['input_dir']}
    Output Directory: {make_cursor_options['output_dir']}

    Size: {make_cursor_options['cursor_size'].pop() or 32}
    Type: {make_cursor_options['cursor_type']}
    Hotspot: {make_cursor_options['cursor_hotspot']}
    Animation Delay: {make_cursor_options['anim_delay']}
    """
