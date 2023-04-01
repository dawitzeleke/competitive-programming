class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        
        current = list(words[0])
        
        for i in range(1, len(words)):
            curr = []
            for letter in words[i]:
                if letter in current:
                    curr.append(letter)
                    current.remove(letter)
            current = curr
            
        return current 