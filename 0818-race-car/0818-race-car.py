from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque()
        visited = set()
        queue.append((0,1, 0))
        visited.add((0,0))
        while queue:
            
            current = queue.popleft()
            position = current[0]
            speed = current[1]
            instruction_len = current[2]
            
            if position == target:
                return instruction_len
            
            tempA_position = position + speed
            tempA_speed = speed * 2
            if (tempA_position, tempA_speed) not in visited:
                visited.add((tempA_position, tempA_speed))
                queue.append((tempA_position, tempA_speed, instruction_len + 1))
            
            tempR_position = position
            tempR_speed = -1 if speed > 0 else 1
            
            if (tempR_position, tempR_speed) not in visited:
                visited.add((tempR_position, tempR_speed))
                queue.append((tempR_position, tempR_speed, instruction_len + 1))
                            
        