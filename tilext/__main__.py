if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Find the tile grid offset in a image.')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), required=True,
                        help='the input image')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='the prefix for the generated files')
    parser.add_argument('-tw', '--tilewidth', type=int, default=16,
                        help='the width of the tiles in pixels')
    parser.add_argument('-th', '--tileheight', type=int, default=16,
                        help='the height of the tiles in pixels')
    parser.add_argument('-tc', '--tilecolors', type=int, default=16,
                        help='the (max) number of colors in a single tile')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

    quit()
    reader = png.Reader(filename='tests/truxton.png')
    w,h,pixels,metadata = reader.read()
    print metadata
    rows = list(pixels)
    tileSizePx=16
    itemsPerPx=3

    offsetFinder = tilext.OffsetFinder(itemsPerPx,tileSizePx,tileSizePx,rows)
    xOffset = offsetFinder.findBestHorizontalOffset()
    yOffset = offsetFinder.findBestVerticalOffset(xOffset)
