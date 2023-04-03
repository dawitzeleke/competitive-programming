class Solution:
    
    def helper(self, current):
        if len(current) == len(self.nums):
            self.result.append(current[:])
            return 
        for num in self.count:
            if self.count[num] > 0:
                current.append(num)
                self.count[num] -= 1
                
                self.helper(current)
                self.count[num] += 1
                current.pop()
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.count = {n : 0 for n in nums}
        for n in nums:
            self.count[n] += 1
        self.nums = nums
        self.result = []
        self.helper([])
        return self.result