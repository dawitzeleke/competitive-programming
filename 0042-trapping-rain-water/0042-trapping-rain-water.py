class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        rightmax = height[len(height) - 1]
        answer = 0
        
        left = 1
        right = len(height) - 2

        while left <= right:
            if leftmax < rightmax:
                answer += max(0, leftmax - height[left])
                leftmax = max(leftmax, height[left])
                left += 1
            else:
                answer += max(0, rightmax - height[right])
                rightmax = max(rightmax, height[right])
                right -= 1
                

        return answer

                