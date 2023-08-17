class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if (query_row, query_glass) == (0, 0):
            return min(1, poured)

        memo = {}        
        def overflow(row, col):
            if (row, col) == (0, 0):
                return max((poured - 1) / 2, 0)
        
            if (row, col) in memo:
                return memo[(row, col)]

            if col > row or col < 0:
                return 0

            memo[(row, col)] = max((overflow(row-1, col-1) + overflow(row-1,col) -1 )/2, 0)
            return memo[(row, col)]

        pour = overflow(query_row-1, query_glass-1) + overflow(query_row-1, query_glass)

        return min(1, pour)
