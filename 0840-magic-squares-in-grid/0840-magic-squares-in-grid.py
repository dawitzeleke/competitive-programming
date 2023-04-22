class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        counter = 0
        
        row = len(grid)
        col = len(grid[0])
        
        def helper(row, col):
           
            main_d = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            sub_d = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
            temp = main_d == sub_d == row1 == row2 == row3 == col1 == col2 == col3 
                
            if not temp:
                return False
            
            nums = set()
            for i in range(row,row + 3):
                for j in range(col,col + 3):
                    nums.add(grid[i][j])
            for num in nums:
                if 0 < num < 10:
                    continue
                else:
                    return False
            length = len(nums)
            if length == 9:
                return True
            return False
        
        for r in range(row - 2):
            for c in range( col - 2):
                if helper(r, c):   
                    counter += 1
                    
        return counter 