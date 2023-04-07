class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
      
        
        for i, j in edges:
            indegree[j] += 1
            
        return [i for i in range(len(indegree)) if indegree[i] == 0]
        