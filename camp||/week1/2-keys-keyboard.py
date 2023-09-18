class Solution:
    def minSteps(self, n: int) -> int:
        count = 0 
        length = 1
        clipboard = 0 
        
        while length < n:
            if n % length == 0:
                count += 1
                clipboard = length
                
            length += clipboard
            count += 1
            
        return count
        