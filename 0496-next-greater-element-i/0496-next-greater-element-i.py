class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [-1] * len(nums2)
        stack = []


        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                    stack.pop()
                
            if stack:
                answer[i] = stack[-1]
            stack.append(nums2[i])

        for i in range (len(nums1)):
            nums1[i] = answer[nums2.index(nums1[i])]

        return nums1