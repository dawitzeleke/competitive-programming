class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike = { i : [] for i in range(1, n + 1)}
        
        for a, b in dislikes:
            dislike[a].append(b)
            dislike[b].append(a)
            
        bipart = [-1] * n
        
        visited = set()
       
        def dfs(node, curr):
            if node not in visited:
                visited.add(node)

                bipart[node - 1] = curr
                for neighbor in dislike[node]:
                    if not dfs(neighbor, 1 - curr):
                        return False
                return True
            
            return bipart[node-1] == curr
        
        for i in range (1, n + 1):
            if i not in visited:
                if not dfs(i, 0):
                    return False
                
        return True