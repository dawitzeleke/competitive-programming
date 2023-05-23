class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = { i : i for i in range(len(s))}
        rank = { i : 1 for i in range(len(s))}
        helper = defaultdict(list)
       
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        
        def Union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]

        for a, b in pairs:
            Union(a, b)
   
        for key, value in parent.items():
          
            par =  find(key)
            helper[par].append(s[key])
            
        answer = ""
        for key in helper:
            helper[key] = sorted(helper[key])
        for i, char in enumerate(s):
            pare = find(i)
            answer += helper[pare][0]
            helper[pare].pop(0)
       
        return answer