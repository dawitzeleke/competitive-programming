class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        denot = { i : [] for i in range(len(bombs))}
        
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j]
                current_distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
                if r1 >= current_distance:
                    denot[i].append(j)
                if r2 >= current_distance:
                    denot[j].append(i)
                    
        self.max_explotion = 1
        visited = set()
        def dfs(node):  
            visited.add(node)
            for neighbor in denot[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        for key in denot:
            dfs(key)
            self.max_explotion = max(self.max_explotion, len(visited))
            visited = set()
        return self.max_explotion 
        