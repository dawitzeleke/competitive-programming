class Solution:
    S = [0] * 201
    vers = 0

    def isGood(self, nums: List[int]) -> bool:
        Solution.vers += 1
        n = len(nums) - 1

        for num in nums:
            if num > n or Solution.S[num] == -Solution.vers: return False

            if Solution.S[num] == Solution.vers:
                if num < n: return False
                Solution.S[num] = -Solution.vers
                continue

            Solution.S[num] = Solution.vers

        return True