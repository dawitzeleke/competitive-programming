class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        prerequisite = defaultdict(set)
        
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        queue = collections.deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            current = queue.popleft()
            
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                prerequisite[neighbor].add(current)
                prerequisite[neighbor].update(prerequisite[current])
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        answer = []
        
        for u, v in queries:
            if u in prerequisite[v]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer