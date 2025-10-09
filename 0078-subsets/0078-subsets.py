class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.answer = []
        self.backtracking(nums, [])
        return self.answer
    def backtracking(self, nums, curr):
        if len(nums) == 0:
            self.answer.append(curr)
            return

        
        self.backtracking(nums[1:], curr + [nums[0]])

        self.backtracking(nums[1:], curr)
        