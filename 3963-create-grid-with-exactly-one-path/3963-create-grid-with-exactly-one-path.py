class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        answer =  [["#"] * n  for _ in range(m)]

        for i in range(n):
            answer[0][i] = "."

        for j in range(m):
            answer[j][n - 1] = "."

        return ["".join(i) for i in answer]