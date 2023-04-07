class Solution:
    
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = { i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        visited = set()
        def dfs(node):
        
            if node in visited:
                return False
            if prereq[node] == []:
                return True
            
            visited.add(node)
            
            for c in prereq[node]:
                if not dfs(c):
                    return False
                
            visited.remove(node)
            prereq[node] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True