class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        currMin = float("inf")
        for i in range(len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            if stack and stack[-1][1] < nums[i]:
                return True
            stack.append([nums[i], currMin])
            currMin = min(currMin, nums[i])
        return False