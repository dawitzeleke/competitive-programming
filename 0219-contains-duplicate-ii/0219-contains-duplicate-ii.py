class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        if k < 1:
            return False
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = i
            else:
                l = abs(i - d[num])
                if l <= k:
                    return True
                d[num] = i
        return False

        
                    