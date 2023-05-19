class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {i: i for i in s1}
        for st in s2:
            parent[st] = st
        rank = { i: i for i, v in parent.items()}
     
        def find(node):
         
            if parent[node] != node:
                parent[node] = find(parent[node])
                
            return parent[node]
        
        def Union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                if rank[p1] < rank[p2]:
                    parent[p2] = p1

                    rank[p1] += rank[p2]

                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
            
        for i in range(len(s1)):
            Union(s1[i], s2[i])
        answer = ''
        for string in baseStr:
            if string not in parent:
                answer += string
            else:
                answer += find(string)
        return answer