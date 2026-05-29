class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        answer = 0
        count = Counter(word)
        visited = set()
        for char in word:
            if ((char.islower() and char.upper() in count) or (char.isupper() and char.lower() in count)) and char.lower() not in visited:
                answer += 1
                visited.add(char.lower())

        return answer