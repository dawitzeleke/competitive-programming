import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while deq and nums[deq[-1]] < nums[i]:
                    deq.pop()
            deq.append(i)
            if i >= k-1:
                ans.append(nums[deq[0]])
                if nums[deq[0]] == nums[i-k+1]:
                    deq.popleft()
        return ans