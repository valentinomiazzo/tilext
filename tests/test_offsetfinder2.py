# Let's make the sources folder importable ...
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import png
import tilext

def test_mac():
    tileSizePx=16
    itemsPerPx=1
    rows = [[0,255,0,1,1,1],
            [2,2,2,0,0,0]]
    offsetFinder = tilext.OffsetFinder2(itemsPerPx,tileSizePx,tileSizePx,rows)
    mac = offsetFinder._mac([0,0],[0,0],[1,0],6)
    assert mac == 0

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
