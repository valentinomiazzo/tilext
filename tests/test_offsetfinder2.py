# Let's make the sources folder importable ...
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import png
import tilext

def test_mac():
    tileSizePx=16
    itemsPerPx=1
    rows = [[0,0,0,1,1,1],
            [2,2,2,0,0,0]]

    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)
    mac = offsetFinder._mac([0,1],[0,0],[1,0],6)

    # 2,2,2,0,0,0
    # 2,2,2,0,0,0
    assert mac == (2-128)*(2-128)*3 + (0-128)*(0-128)*3

def test_mac_with_offset():
    tileSizePx=16
    itemsPerPx=1
    rows = [[0,0,0,1,1,1],
            [2,2,2,0,0,0]]

    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)
    mac = offsetFinder._mac([0,1],[1,0],[1,0],6)

    # 2,2,2,0,0,0
    # x 2,2,2,0,0,0
    # - - - - - -
    assert mac == (2-128)*(2-128)*2 + (0-128)*(2-128)*2 + (0-128)*(0-128)*2

def test_mac_with_negative_offset():
    tileSizePx=16
    itemsPerPx=1
    rows = [[0,0,0,1,1,1],
            [2,2,2,0,0,0]]

    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)
    mac = offsetFinder._mac([0,1],[-1,0],[1,0],6)

    #   2,2,2,0,0,0
    # 2,2,2,0,0,0 x
    #   - - - - - -
    assert mac == (2-128)*(2-128)*2 + (0-128)*(2-128) + (0-128)*(0-128)*3

def test_mac_vertical():
    tileSizePx=16
    itemsPerPx=1
    rows = [[000,0],
            [127,1],
            [255,2]]

    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)
    mac = offsetFinder._mac([0,0],[0,0],[0,1],3)

    # 000, 127, 255
    # 000, 127, 255
    assert mac == (000-128)**2 + (127-128)**2 + (255-128)**2

def test_mac_vertical_with_offset():
    tileSizePx=16
    itemsPerPx=1
    rows = [[000,0],
            [127,1],
            [255,2]]

    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)
    mac = offsetFinder._mac([0,0],[0,1],[0,1],3)

    # 000, 127, 255
    # xxx  000, 127, 255
    # ---  ---  ---
    assert mac == (000-128)**2 + (127-128)*(000-128) + (255-128)*(127-128)

def test_arePixelsEqual():
    tileSizePx=16
    itemsPerPx=3
    rows = [[0,0,0,  1,1,1],
            [2,2,2,  0,0,0]]
    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)

    result = offsetFinder._arePixelsEqual([0,0], [1,1])
    assert result == True

    result = offsetFinder._arePixelsEqual([0,0], [0,1])
    assert result == False

def test_areSliceEqual():
    tileSizePx=2
    itemsPerPx=3
    rows = [[0,0,0, 1,1,1, 0,0,0, 1,1,1],
            [0,0,0, 1,1,1, 2,2,2, 0,0,0],
            [0,0,0, 1,1,1, 0,0,0, 1,1,1],
            [0,0,0, 1,1,1, 2,2,2, 0,0,0]]
    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)

    result = offsetFinder._areSlicesEqual([0,0], [2,0], [1,0])
    assert result == True

    result = offsetFinder._areSlicesEqual([0,0], [2,1], [1,0])
    assert result == False

    result = offsetFinder._areSlicesEqual([0,0], [0,2], [0,1])
    assert result == True

    result = offsetFinder._areSlicesEqual([0,0], [1,2], [0,1])
    assert result == False
