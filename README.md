# ClickGen Batch Converter

## Usage

``` Shell
python clickgen_batch_converter.py [-h] -i INPUT_DIR -o OUTPUT_DIR -p {windows,x11} -t {static,animated} [-s CURSOR_SIZE] [-x HOTSPOT_X] [-y HOTSPOT_Y] [-d ANIM_DELAY]
```

### Options

Path to a directory with cursor files in PNG format

``` Shell
-i, --input-dir INPUT_DIR
```

Output directory for the cursor files

``` Shell
 -o, --output-dir OUTPUT_DIR
```

Target system platform. Options: `windows`, `x11`

``` Shell
-p, --platform {windows,x11}
```

Cursor type. Options: `static`, `animated`

``` Shell
-t, --cursor-type {static,animated}
```

Cursor size, the following pattern can be used to enable canvasing: `size:canvas_size`. Default: 32

``` Shell
-s, --cursor-size CURSOR_SIZE
```

Hotspot value to be used in the X axis. Default: 5

``` Shell
-x, --hotspot-x HOTSPOT_X
```

Hotspot value to be used in the Y axis. Default: 5

``` Shell
-y, --hotspot-y HOTSPOT_Y
```

 Animation delay to be used for animated cursors. Default: 1

``` Shell
-d, --anim-delay ANIM_DELAY
```

Show a help message and exit

``` Shell
-h, --help
```

### Install Dependencies

``` Shell
python -m pip install -r requirements.txt
```
