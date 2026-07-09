class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff:int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n

        curr = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr += 1
            component[i] = curr

        return [
            component[u] == component[v]
            for u, v in queries
        ]