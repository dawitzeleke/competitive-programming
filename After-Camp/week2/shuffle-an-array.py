import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums
    def shuffle(self) -> List[int]:
        temp = self.nums.copy()
        random.shuffle(temp)
        return temp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()