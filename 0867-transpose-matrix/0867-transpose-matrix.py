class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        res = []
        for j in range(col):
            temp = []
            for i in range(row):
                temp.append(matrix[i][j])
            res.append(temp)        
    
        return res