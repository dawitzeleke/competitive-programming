class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        answer = float("inf")

        while left <= right:
            mid = left + (right - left) // 2

            if nums[left] <= nums[mid]:
                answer = min(nums[left], answer)
                left = mid + 1

            else:
                answer = min(nums[mid], answer)

                right = mid - 1
        return answer
