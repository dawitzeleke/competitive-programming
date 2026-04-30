class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        print(count)
        answer = [0, 0]

        for i in range(1, n + 1):
            if count[i] == 2:
                answer[0] = i
            if count[i] == 0:
                answer[1] = i
        return answer