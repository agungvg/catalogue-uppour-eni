"""UPPOUR -- the kettle that pours upwards.

Entry for "The Catalogue Photo of an Impossible Gadget"
(make.fun, the-catalogue-photo-of-an-2-20261121-0341).

The entry image is a studio catalogue photograph generated during the
build and shipped in this repository as entry.png. This program is
fully deterministic: it performs no network access, reads no clock,
uses no randomness, and simply copies the shipped image to the
output location required by the competition harness.

Output: $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_png_dimensions(path):
    """Return (width, height) of a PNG by parsing its IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    src_size = os.path.getsize(SOURCE)
    dst_size = os.path.getsize(dest)
    if src_size != dst_size:
        print(f"size mismatch: source {src_size} != dest {dst_size}",
              file=sys.stderr)
        return 1
    if dst_size > MAX_BYTES:
        print(f"output too large: {dst_size} > {MAX_BYTES} bytes",
              file=sys.stderr)
        return 1
    width, height = read_png_dimensions(dest)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"output too large: {width}x{height} > "
              f"{MAX_DIMENSION}x{MAX_DIMENSION}", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({dst_size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
