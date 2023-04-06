class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connection = defaultdict(list)
        unique = set()
        for i in range(len(edges)):
            
            connection[edges[i][0]].append(edges[i][1])
            connection[edges[i][1]].append(edges[i][0])
            unique.add(edges[i][1])
            unique.add(edges[i][0])
        for key, value in connection.items():
            if len(value) == len(unique) - 1:
                return key 
            
        
            