class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col = len(strs[0])
        row = len(strs)
        answer = 0
        for i in range(col):
            for j in range (1, row):
                if strs[j][i] < strs[j-1][i]:
                    answer += 1
                    break
        return answer