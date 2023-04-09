"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        sub = {}
        importance = {}
        
        for employ in employees:
            sub[employ.id] = employ.subordinates
            importance[employ.id] = employ.importance
          
        visited = set()
        self.total_importance = 0
        def dfs(id_):
            if id_ in visited:
                return
            visited.add(id_)
            
            self.total_importance += importance[id_]
            for s in sub[id_]:
                dfs(s)
                
                
        dfs(id)   
        return self.total_importance