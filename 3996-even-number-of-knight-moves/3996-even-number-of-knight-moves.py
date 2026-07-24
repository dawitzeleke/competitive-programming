class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return sum(start + target) % 2 == 0
