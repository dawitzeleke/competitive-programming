class Solution(object):
    def pancakeSort(self, A):
        result = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            result.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return result
