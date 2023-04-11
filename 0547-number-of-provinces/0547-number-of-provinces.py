class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = { i : [] for i in range(1, len(isConnected[0]) + 1)}
        visited = set()
        def dfs(node):
            stack = []
            stack.append(node)
            visited.add(node)
            while stack:
                temp = stack.pop()
                for n in count[temp]:
                    if n not in visited:
                        stack.append(n)
                        visited.add(n)
            
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if r != c:
                    if isConnected[r][c] == 1:
                        count[r + 1].append(c + 1)
                        count[c + 1].append(r + 1)
        answer = 0                
        
        for i in range(1, len(isConnected[0]) + 1):
            if i not in visited:
                dfs(i)
                answer += 1

        return answer