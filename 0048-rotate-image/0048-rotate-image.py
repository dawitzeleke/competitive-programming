class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            
            for c in range(r, col):
                
                 matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
                    
                    
            matrix[r].reverse()
            
        return matrix