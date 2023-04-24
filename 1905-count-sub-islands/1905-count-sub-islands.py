class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col  = len(grid1), len(grid1[0])
        visited = set()
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == row or c == col or grid2[r][c] == 0 or (r,c) in visited:
                return True
            
            visited.add((r,c))
            dirc = [[1,0], [0,1], [-1,0], [0,-1]] 
            temp = True
            if grid1[r][c] == 0:
                temp = False
                
            for dr, dc in dirc:
                temp = dfs(r + dr, c + dc) and temp
                
            return temp
        result = 0
        
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid2[r][c] != 0 and dfs(r,c):
                    result += 1
                    
        return result