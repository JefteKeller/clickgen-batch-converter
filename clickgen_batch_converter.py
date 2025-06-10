from common.aliases import MakeCursorOptions
from common.utils import get_cmd_args
from handlers import make_cursors


def main() -> None:
    args = get_cmd_args()

    make_cursor_options: MakeCursorOptions = {
        'input_dir': args.input_dir,
        'output_dir': args.output_dir,
        'platform': args.platform,
        'cursor_type': args.cursor_type,
        'cursor_size': args.cursor_size,
        'cursor_hotspot': (args.hotspot_x, args.hotspot_y),
        'anim_delay': args.anim_delay,
    }

    make_cursors(make_cursor_options)

    return print('Operation complete.')


if __name__ == "__main__":
    main()
