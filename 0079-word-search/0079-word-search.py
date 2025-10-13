class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        path = set()
        def isValidGrid(r, c):
            return r >= 0 and r < row and c >= 0 and c < col

        def dfs(r, c, i):

            if i == len(word):
                return True

            if  not isValidGrid(r, c) or board[r][c] != word[i] or (r, c) in path:
                return False
            path.add((r, c))
            res = False
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                res = res or dfs(new_r, new_c, i + 1)
            path.remove((r, c))
            return res
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False