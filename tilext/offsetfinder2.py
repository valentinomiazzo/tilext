import operator

class OffsetFinder2:

    # A Tile is made of N*N Pixels
    # A Tile has N Rows
    # A Row is composed of N pixels
    # A Pixel is made of M Elements
    # A sequence of N*M Elements is called Slice

    def __init__(self, itemsPerPx, tileWidthPx, tileHeightPx, rows):
        self.ITEMS_PER_PX = itemsPerPx
        self.PX_PER_SLICE = tileWidthPx
        self.ITEMS_PER_SLICE = tileWidthPx * itemsPerPx
        self.ROWS_PER_TILE = tileHeightPx
        self.rows = rows

    def _mac(self, start, offset, delta, length):
        xa = start[0]
        ya = start[1]
        xb = xa + offset[0]
        yb = ya + offset[1]
        ix = 0
        iy = 0
        dx = delta[0]
        dy = delta[1]
        mac = 0
        for i in range(0, length):
            a = self.rows[ya + iy][xa + ix] - 128
            print a
            b = self.rows[yb + iy][xb + ix] - 128
            print b
            mac += a*b
            print mac
            ix += dx
            iy += dy
        return mac

    def _arePixelsEqual(self, a, b):
        result = True
        rowA = self.rows[a[1]]
        idxA = a[0] * self.ITEMS_PER_PX
        rowB = self.rows[b[1]]
        idxB = b[0] * self.ITEMS_PER_PX
        for i in range(0, self.ITEMS_PER_PX):
            if rowA[idxA+i] != rowB[idxB+i]:
                result = False
                break
        return result

    def _areSlicesEqual(self, a, b, delta):
        result = True
        ax = a[0]
        ay = a[1]
        bx = b[0]
        by = b[1]
        dx = delta[0]
        dy = delta[1]
        for i in range(0, self.PX_PER_SLICE):
            if not self._arePixelsEqual([ax,ay], [bx,by]):
                result = False
                break
            ax += dx
            bx += dx
            ay += dy
            by += dy
        return result

    def findBestHorizontalOffset(self):
        counters = {}
        for row in self.rows:
            self.__checkHorizontalOffsetsPerRow(counters, row)
        return OffsetFinder.__extractBestOffset(counters)

    @staticmethod
    def __extractBestOffset(counters):
        sortedCounters = sorted(counters.items(), key=operator.itemgetter(1), reverse=True)
        bestOffset = sortedCounters[0][0]
        return int(bestOffset)

    def __checkHorizontalOffsetsPerRow(self, counters, row):
        for xOffsetPx in range(0, self.PX_PER_SLICE):
            count = self.__countSlicesRepetitionsPerRow(row, xOffsetPx * self.ITEMS_PER_PX)
            OffsetFinder.__incCounter(counters, xOffsetPx, count)

    @staticmethod
    def __incCounter(counters, item, amount):
        if str(item) in counters:
            counters[str(item)] += amount
        else:
            counters[str(item)] = amount

    def __countSlicesRepetitionsPerRow(self, row, slicesOffset):
        counter = 0
        referenceSliceIdx = slicesOffset
        # When slicesOffset != 0 we have to skip the last slice because incomplete.
        # Anyway, we skip it even when slicesOffset == 0 because otherwise offset zero would
        # have more chances to find matches and this would un-balance the search towards it.
        while referenceSliceIdx < len(row) - self.ITEMS_PER_SLICE:
            counter += self.__countSliceMatchesPerRow(row, slicesOffset, referenceSliceIdx)
            referenceSliceIdx += self.ITEMS_PER_SLICE
        return counter

    def __countSliceMatchesPerRow(self, row, slicesOffset, referenceSliceIdx):
        counter = 0
        targetSliceIdx = slicesOffset
        # See comment in __countSlicesRepetitionsPerRow
        while targetSliceIdx < len(row) - self.ITEMS_PER_SLICE:
            if self.__areSlicesEqual(row, referenceSliceIdx, row, targetSliceIdx):
                counter += 1
            targetSliceIdx += self.ITEMS_PER_SLICE
        return counter

    def __areSlicesEqual(self, referenceSliceRow, referenceSliceIdx, targetSliceRow, targetSliceIdx):
        isMatching = True
        for i in range(0,self.ITEMS_PER_SLICE):
            if referenceSliceRow[referenceSliceIdx+i] != targetSliceRow[targetSliceIdx+i]:
                isMatching = False
                break
        return isMatching

    def findBestVerticalOffset(self, xOffsetPx):
        counters = {}
        columnSliceIdx = xOffsetPx * self.ITEMS_PER_PX
        # See comment in __countSlicesRepetitionsPerRow
        while columnSliceIdx < len(self.rows[0]) - self.ITEMS_PER_SLICE:
            self.__checkVerticalOffsetsPerColumn(counters, columnSliceIdx)
            columnSliceIdx += self.ITEMS_PER_SLICE
        return OffsetFinder.__extractBestOffset(counters)

    def __checkVerticalOffsetsPerColumn(self, counters, slicesOffset):
        for yOffsetRows in range(0, self.ROWS_PER_TILE):
            count = self.__countTilesRepetitionsPerColumn(slicesOffset, yOffsetRows)
            OffsetFinder.__incCounter(counters, yOffsetRows, count)

    def __countTilesRepetitionsPerColumn(self, slicesOffset, rowsOffset):
        counter = 0
        referenceRowIdx = rowsOffset
        # See comment in __countSlicesRepetitionsPerRow
        while referenceRowIdx < len(self.rows) - self.ROWS_PER_TILE:
            counter += self.__countTileMatchesPerColumn(slicesOffset, rowsOffset, referenceRowIdx)
            referenceRowIdx += self.ROWS_PER_TILE
        return counter

    def __countTileMatchesPerColumn(self, slicesOffset, rowsOffset, referenceRowIdx):
        counter = 0
        targetRowIdx = rowsOffset
        # See comment in __countSlicesRepetitionsPerRow
        while targetRowIdx < len(self.rows) - self.ROWS_PER_TILE:
            if self.__areTilesEqual(slicesOffset, targetRowIdx, referenceRowIdx):
                counter += 1
            targetRowIdx += self.ROWS_PER_TILE
        return counter

    def __areTilesEqual(self, slicesOffset, referenceTileRowIdx, targetTileRowIdx):
        isMatching = True
        for i in range(0,self.ROWS_PER_TILE):
            if not self.__areSlicesEqual(self.rows[referenceTileRowIdx+i], slicesOffset, self.rows[targetTileRowIdx+i], slicesOffset):
                isMatching = False
                break
        return isMatching

if __name__ == '__main__':
    pass
