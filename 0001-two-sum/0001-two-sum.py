class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminder = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff not in reminder:
                reminder[nums[i]] = i

            else:

                return [reminder[diff], i]

        
            