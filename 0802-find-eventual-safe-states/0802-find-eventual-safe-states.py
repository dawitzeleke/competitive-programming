class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0] * len(graph)
        grap = defaultdict(list)
        ans = []
        queue = collections.deque()
       
        for i in range(len(graph)):
            for neighbor in graph[i]:
                grap[neighbor].append(i)
                indegree[i] += 1
        
        for i, a in enumerate(graph):
            if len(a) == 0:
                queue.append(i)
                
        while queue:
            temp = queue.popleft()
            ans.append(temp)
            for neighbor in grap[temp]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        ans.sort()
        return ans