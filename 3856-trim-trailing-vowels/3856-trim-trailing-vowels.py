class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]


        for i in range(len(s) - 1, -1, -1):
            if s[i] in vowels:
                s = s[:i]

            else:
                break

        return s