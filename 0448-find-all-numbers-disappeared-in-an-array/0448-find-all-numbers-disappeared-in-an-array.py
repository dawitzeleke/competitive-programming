class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]

        for i, num in enumerate(nums):
            if num > 0:
                answer.append(i + 1)

        return answer