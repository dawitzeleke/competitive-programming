class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        r = 0
        c = len(matrix[0]) - 1
        while c >= 0 and r < row:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False