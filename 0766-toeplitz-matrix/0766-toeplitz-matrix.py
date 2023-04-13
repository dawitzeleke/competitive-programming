class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row -1, -1, -1):
            
            temp = matrix[i][0]
            left = 0
            top = i
            while top < row and left < col:
                if matrix[top][left] != temp:
                    return False
                top += 1
                left += 1
        for i in range(col):
            temp2 = matrix[0][i]
            lef = i
            to = 0
            while to < row and lef < col:
                if matrix[to][lef] != temp2:
                    return False
                to += 1
                lef += 1
            
        return True