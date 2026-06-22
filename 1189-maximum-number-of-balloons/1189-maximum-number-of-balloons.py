from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)
        max_count = 0

        while True:
            if (char_count.get("b", 0) < 1) or (char_count.get("a", 0) < 1 ) or (char_count.get("n", 0) < 1) or (char_count.get("l", 0) < 2) or (char_count.get("o", 0) < 2):
                break
            
            max_count += 1

            char_count["b"] -= 1
            char_count["a"] -= 1
            char_count["n"] -= 1
            char_count["l"] -= 2
            char_count["o"] -= 2
        return max_count