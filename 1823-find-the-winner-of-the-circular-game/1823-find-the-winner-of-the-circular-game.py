class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = collections.deque([i for i in range(1, n + 1)])
       
        while len(nums) > 1:
            for i in range (k - 1):
                num = nums.popleft()
                nums.append(num)
            nums.popleft()
            
        return nums.popleft()