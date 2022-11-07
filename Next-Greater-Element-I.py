class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
       
        need, ready, next_greater = set(nums1), set(), {}
        for n in nums2:
            for k in ready:
                if k < n:
                    next_greater[k] = n
            ready = {k for k in ready if k not in next_greater}
            if n in need and n not in next_greater and n not in ready:
                ready.add(n)
        return [next_greater[k] if k in next_greater else -1 for k in nums1]   
