# Let's make the sources folder importable ...
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

if __name__ == '__main__':

    import png
    import tilext
    import argparse

    parser = argparse.ArgumentParser(description='Find the tile grid offset in a image.')
    parser.add_argument('-i', '--input', type=str, required=True,
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
    #print args

    reader = png.Reader(filename=args.input)
    w,h,pixels,metadata = reader.read()
    rows = list(pixels)
    print metadata
    if metadata['bitdepth'] != 8:
        sys.stderr.write('ERROR: PNG with bitdepth != 8\n')
        sys.stderr.write(str(metadata))
        sys.exit(1)

    itemsPerPx=metadata['planes']

    offsetFinder = tilext.OffsetFinder(itemsPerPx, args.tilewidth, args.tileheight, rows)
    xOffset = offsetFinder.findBestHorizontalOffset()
    print xOffset
    yOffset = offsetFinder.findBestVerticalOffset(xOffset)
    print yOffset
