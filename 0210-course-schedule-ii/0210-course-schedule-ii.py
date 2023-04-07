class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        result = []
        visited = set()
        cycle = set()
        def dfs(node):
        
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            
            for c in prereq[node]:
                if not dfs(c):
                    return False
                
            cycle.remove(node)
            visited.add(node)
            result.append(node)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return result