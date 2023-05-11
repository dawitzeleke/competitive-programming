class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
      
        indegree = [0] * n
        graph = defaultdict(list)
        ans = [ set() for _ in range(n)]
        
        queue = collections.deque()
       
        for f, t in edges:
            graph[f].append(t)
            indegree[t] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            temp = queue.popleft()
            
            for neighbor in graph[temp]:
                indegree[neighbor] -= 1
                ans[neighbor].add(temp)
                ance = ans[neighbor].union(ans[temp])
                ans[neighbor] = ance
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        for i in range(len(ans)):
            ans[i] = sorted(list(ans[i]))
        return ans