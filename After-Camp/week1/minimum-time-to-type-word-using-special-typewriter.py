class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        prev = 'a'
        for char in word:
            dist = abs(ord(char) - ord(prev))
            res += min(dist, 26 - dist)
            prev = char
        return res