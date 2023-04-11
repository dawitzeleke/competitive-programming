class Solution:
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        counter = { i : [] for i in range(len(graph))}
        for j in range(len(graph)):
            counter[j] = graph[j]
            
        res = []
        self.n = len(graph)
        print(counter)
        def dfs(node, path):
            
            path.append(node)

            if node == self.n - 1 and path not in res:
                res.append(path[:])
                return
            for neighbor in counter[node]:
                dfs(neighbor, path)
                path.remove(neighbor)
                
        dfs(0, [])
        return res