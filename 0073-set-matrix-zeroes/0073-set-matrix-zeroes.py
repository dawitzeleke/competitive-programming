class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_element = []
            
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_element.append((i,j))
        for x, y in zero_element:
            for i in range(m):
                matrix[i][y] = 0
            for j in range(n):
                matrix[x][j] = 0