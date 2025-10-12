class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])
        self.prefixSum = [[0] * (self.n + 1) for _ in range(self.m + 1)]


        for r in range(self.m):
            for c in range(self.n):
                curr_prefix = self.matrix[r][c]

                if self.isValidGrid(r, c - 1):
                    curr_prefix += self.prefixSum[r][c - 1]

                if self.isValidGrid(r - 1, c):
                    curr_prefix += self.prefixSum[r - 1][c]

                if self.isValidGrid(r - 1, c - 1):
                    curr_prefix -= self.prefixSum[r - 1][c - 1]

                self.prefixSum[r][c] = curr_prefix


    def isValidGrid(self, row, col):
        if 0 <= row < self.m and 0 <= col < self.n:
            return True

        return False

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        curr_sum = self.prefixSum[row2][col2]

        if self.isValidGrid(row2, col1 - 1):
            curr_sum -= self.prefixSum[row2][col1 - 1] 

        if self.isValidGrid(row1 - 1, col2):
            curr_sum -= self.prefixSum[row1 - 1][col2]

        if self.isValidGrid(row1 - 1, col1 - 1):
            curr_sum += self.prefixSum[row1 - 1][col1 - 1]

        
        return curr_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)