class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        
        indegree = [0] * len(quiet)
        
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        queue = collections.deque()
        answer = list(range(len(quiet)))
        
        for i, num in enumerate(indegree):
            if num == 0:
                queue.append(i)
        while queue:
            current = queue.popleft()
            
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                q = quiet[answer[neighbor]]
                q2 = quiet[answer[current]]
                if q > q2:
                    answer[neighbor] = answer[current]
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return answer