class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(float("-inf"))
        max_rec = 0
        for i in range (len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                max_rec = max(max_rec, (right - left - 1)*heights[temp])
            stack.append(i)
        return max_rec
        