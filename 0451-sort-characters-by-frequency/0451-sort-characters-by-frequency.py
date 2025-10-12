class Solution:
    def frequencySort(self, s: str) -> str:
        

        count = Counter(s)

        temp = []
        answer = ""

        for char, c in count.items():
            temp.append([c, char])

        temp.sort(reverse=True)
        for c, char in temp:
            answer += c * char

        return answer


