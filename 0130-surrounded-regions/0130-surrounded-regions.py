class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = len(board)
        col = len(board[0])
        visited = set()

        # is valid row and column pair

        # define the directions
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # define the dfs function

        def dfs(r, c):
            if r < 0 or c < 0 or r > row - 1 or c > col - 1 or (r, c) in visited or board[r][c] != "O" :
                return

            visited.add((r, c))

            for row_c, col_c in directions:
                new_row = r + row_c
                new_col = c + col_c

                dfs(new_row, new_col)

        
        for i in range(row):

            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][col - 1] == "O":
                dfs(i, col - 1)

        for j in range(col):

            if board[0][j] == "O":
                dfs(0, j)
            if board[row - 1][j] == "O":
                dfs(row - 1, j)


        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"

                     

