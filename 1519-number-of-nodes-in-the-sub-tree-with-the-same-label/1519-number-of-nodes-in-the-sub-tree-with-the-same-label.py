class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        con = {i : [] for i in range(n)}
        for x, y in edges:
            con[x].append(y)
            con[y].append(x)
            
        ans = [0]*n
        self.n = n
    
        
        def dfs(node, parent):
            counts = collections.Counter()
            counts[labels[node]] += 1
            
            for n in con[node]:
                if n != parent:
                    counts += dfs(n, node)
                    
            ans[node] = counts[labels[node]]
            return counts
            
           
        dfs(0, None)
        return ans