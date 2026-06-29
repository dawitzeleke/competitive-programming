class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        count = 0 

        for char in patterns:
            if char in word:
                count += 1

        return count