class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        start = 0
        mid = 0
        end = len(nums) - 1


        while mid <= end:

            if nums[mid] == 0:
                nums[mid], nums[start] = nums[start], nums[mid]
                mid += 1
                start += 1
            elif nums[mid] == 1:

                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
