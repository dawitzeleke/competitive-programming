class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        start = image[sr][sc]
        visited = set()
        def dfs(r, c):
            directions = [[0,0], [1,0], [0,1], [-1, 0], [0, -1]]
            queue = collections.deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    rn = r + dr
                    cn = c + dc
                    if  rn < row and rn >= 0 and cn < col and cn >= 0 and (rn, cn) not in visited and image[rn][cn] == start :
                        image[rn][cn] = color
                        visited.add((rn, cn))
                        queue.append((rn, cn))
        dfs(sr, sc)
        return image