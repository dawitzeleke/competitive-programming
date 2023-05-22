class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        for num in nums1:
            if num in nums2:
                ans.add(num)
                
        return ans