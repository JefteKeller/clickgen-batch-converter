import argparse


def get_cmd_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'input_dir',
        type=str,
        help='Path to a directory with cursor files in PNG format.',
    )

    parser.add_argument(
        '-o',
        '--output-dir',
        type=str,
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
        type=int,
        default=5,
        help='Hotspot value to be used in the X axis. Default: "%(default)s"',
    )

    parser.add_argument(
        '-y',
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
