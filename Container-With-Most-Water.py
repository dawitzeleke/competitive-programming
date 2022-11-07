class Solution(object):
    def maxArea(self, height):
        p1 = 0  
        p2 = len(height) - 1 
        max_area = 0
        while p1 != p2:
            if height[p1] > height[p2]:
                area = height[p2] * (p2 - p1) 
                p2 -= 1 
            else:
                area = height[p1] * (p2 - p1)
                p1 += 1
            if area > max_area: max_area = area 
        return max_area
        
