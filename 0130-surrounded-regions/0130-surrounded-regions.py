class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col  = len(board), len(board[0])
        
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == row or c == col or board[r][c] != "O":
                return 
            
            dirc = [[1,0], [0,1], [-1,0], [0,-1]] 
            if board[r][c] == "O":
                board[r][c] = "T"
            
            for dr, dc in dirc:
                dfs(r + dr, c + dc)
        
        for i in range(col):
            if board[0][i] == 'O': 
                dfs(0, i)
            if board[row-1][i] == 'O': 
                dfs(row-1, i)
                
        for i in range(row):
            if board[i][0] == 'O': 
                dfs(i, 0)
            if board[i][col-1] == 'O':
                dfs(i, col-1)
            
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                
                    
        return board
        