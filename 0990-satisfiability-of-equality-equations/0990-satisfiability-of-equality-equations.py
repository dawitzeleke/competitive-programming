class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(character):chr(character) for character in range(ord("a"), ord("z")+1)}
        rank = {chr(character): 1 for character in range(ord("a"), ord("z")+1)}
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
                
            return parent[node]
        
        def Union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
        for equ in equations:
            if equ[1] == "=":
                Union(equ[0], equ[-1])
                
        for equ in equations:
            if equ[1] == "!":
                if find(equ[0]) == find(equ[-1]):
                    return False
                
        return True