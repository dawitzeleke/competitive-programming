class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        answer = []

        for num, countt in count.items():
            if countt == 2:
                answer.append(num)

        return answer