class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        queue = collections.deque()
        visited = set()
        queue.append(("0000", 0))
        visited.add("0000")
        
        while queue:
            current_key, current_turn = queue.popleft()
            current_turn += 1
            for i in range(4):
                pattern = list(current_key)
                temp = pattern[i]
                
                option1 = int(temp) + 1 if int(temp) != 9 else 0
                option2 = int(temp) - 1 if int(temp) != 0 else 9
                
                pattern[i] = str(option1)
                newpattern = "".join(pattern)
                if newpattern == target:
                    return current_turn 
                if newpattern not in deadends and newpattern not in visited:
                    queue.append((newpattern, current_turn))
                    visited.add(newpattern)
                    
                pattern[i] = str(option2)
                newpattern = "".join(pattern)
                if newpattern == target:
                    return current_turn 
                if newpattern not in deadends and newpattern not in visited:
                    queue.append((newpattern, current_turn))
                    visited.add(newpattern)
        return -1