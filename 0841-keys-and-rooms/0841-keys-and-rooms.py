from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        helper = defaultdict(list)
        for i, r in enumerate(rooms):
            helper[i] = r
        
        
        visited = set()
        queue = deque()
        visited.add(0)
        queue.append(0)
        while queue:
            node = queue.popleft()
            for neighbour in helper[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                        
        if len(visited) == len(rooms):
            return True
        else:
            return False