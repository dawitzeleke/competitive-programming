class Solution(object):
    def diagonalSum(self, mat):
        summ = 0
        
        for i in range(len(mat)):
            if i == len(mat) - i - 1:
                summ += mat[i][i]
            else:
                summ += mat[i][i]+mat[i][len(mat) - i - 1] 
        return summ