class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[length - 1] > nums[length - 2]:
            return length - 1

        left = 1

        right = length - 2

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            elif nums[mid] > nums[mid - 1]:
                left = mid + 1 

            else:
                right = mid - 1

        

        