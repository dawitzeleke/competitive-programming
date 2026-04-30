class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        index = {}
        answer = []
        for i, num in enumerate(temp):
            if num not in index:
                index[num] = i
        for num in nums:
            answer.append(index[num])
        return answer