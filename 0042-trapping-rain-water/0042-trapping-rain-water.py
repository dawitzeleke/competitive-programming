class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        length = len(height)
        left = 1 
        right = length - 2

        maxRight = height[length - 1]
        maxLeft = height[0]

        while left <= right:

            if maxLeft <= maxRight:
                if maxLeft - height[left] > 0:
                    total += maxLeft - height[left]
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                if maxRight - height[right] > 0:
                    total += maxRight - height[right]
                maxRight = max(maxRight,height[right])
                right -= 1

        return total
