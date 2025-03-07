class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        answer = [0, 0]

        freq = [0] * ((n * n) + 1)
        for row in range(n):
            for col in range(n):
                freq[grid[row][col]] += 1

        for i in range(1, ((n * n) + 1)):
            if freq[i] == 0:
                answer[1] = i
            if freq[i] == 2:
                answer[0] = i

        return answer
