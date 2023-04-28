class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        queue = deque()
        visited = set()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        direction = [[1,0], [0,-1], [0,1], [-1,0]]

        while queue:
            temp = queue.popleft()
            x = temp[0]
            y = temp[1]
            d = temp[2]
            for dr, dc in direction:
                
                r = x + dr
                c = y + dc
                if 0 <= r <= row - 1 and 0 <= c <= col - 1  and (r, c) not in visited:
                    visited.add((r,c))
                    queue.append((r, c, d + 1))
                    mat[r][c] = d + 1

        
        return mat