class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_num = max(nums)
        min_num = min(nums)

        answer = []

        for num in range(min_num, max_num + 1):
            if num not in nums:
                answer.append(num)


        return answer