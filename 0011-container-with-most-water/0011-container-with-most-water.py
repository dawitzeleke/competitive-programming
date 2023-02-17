class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_cont = 0
        while r>l:
            vol = (r-l) *min(height[l],height[r])
            max_cont = max(max_cont, vol)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -=1
                
        return max_cont