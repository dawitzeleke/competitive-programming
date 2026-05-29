from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        answer = 0
        last_lower = {}
        first_upper = {}

        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i          # keep overwriting → last occurrence
            elif char.isupper() and char not in first_upper:
                first_upper[char] = i         # only store once → first occurrence

        for char, index in last_lower.items():
            if char.upper() in first_upper and index < first_upper[char.upper()]:
                answer += 1

        return answer