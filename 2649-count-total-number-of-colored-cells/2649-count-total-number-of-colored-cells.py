class Solution:
    def coloredCells(self, n: int) -> int:
        answer = 1

        for i in range(n):
            answer += 4 * i

        return answer