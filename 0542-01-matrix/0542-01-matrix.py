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
            current_row = temp[0]
            current_col = temp[1]
            distance = temp[2]
            for dr, dc in direction:
                
                new_row = current_row + dr
                new_col = current_col + dc
                
                if 0 <= new_row <= row - 1 and 0 <= new_col <= col - 1  and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, distance + 1))
                    mat[new_row][new_col] = distance + 1

        
        return mat