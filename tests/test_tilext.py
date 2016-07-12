# Let's make the sources folder importable ...
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import png
import tilext

def createTiles(w,h,tw,th,xo,yo,epp):
    # 11101110...
    # 11101110...
    # 11101110...
    # 00000000...
    # 11101110...
    # 11101110...
    # 11101110...
    # 00000000...
    # ...........
    def shader(e,y):
        x = e / epp
        tx = (x-xo) / tw
        ty = (y-yo) / th
        v = ((tx+1) * (ty+1)) % 3
        return 255 if v else 0

    rows = [[shader(e,y) for e in range(0,w*epp)] for y in range(0,h)]
    return rows

def test_offset_from_generated_pixels():
    return
    tileSizePx=16
    itemsPerPx=3
    w=tileSizePx*16
    h=tileSizePx*16
    xOffset=5
    yOffset=9
    rows = createTiles(w,h,tileSizePx,tileSizePx,xOffset,yOffset,itemsPerPx)

    offsetFinder = tilext.OffsetFinder(itemsPerPx,tileSizePx,tileSizePx,rows)
    xOffsetFound = offsetFinder.findBestHorizontalOffset()
    yOffsetFound = offsetFinder.findBestVerticalOffset(xOffsetFound)

    assert xOffset == xOffsetFound
    assert yOffset == yOffsetFound

def test_offset_from_png():
    return
    reader = png.Reader(filename='tests/truxton.png')
    w,h,pixels,metadata = reader.read()
    print metadata
    rows = list(pixels)
    tileSizePx=16
    itemsPerPx=3

    offsetFinder = tilext.OffsetFinder(itemsPerPx,tileSizePx,tileSizePx,rows)
    xOffset = offsetFinder.findBestHorizontalOffset()
    yOffset = offsetFinder.findBestVerticalOffset(xOffset)

    assert xOffset == 12
    assert yOffset == 5
