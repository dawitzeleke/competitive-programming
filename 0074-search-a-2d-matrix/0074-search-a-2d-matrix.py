class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        h = len(m) - 1
        l = 0 
        while h >= l:
            mid = (h + l )// 2
            if m[mid][0] > target:
                h = mid - 1
            elif m[mid][-1] < target:
                l = mid + 1
            else: 
                break
                
        left = 0
        right = len(m[0]) - 1
        
        while right >= left :
            temp = (right + left)// 2
            
            if m[mid][temp] > target:
                right = temp - 1
            elif m[mid][temp] < target:
                left = temp + 1
            else:
                return True
        return False