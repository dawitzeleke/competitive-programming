class Solution:
    
    result = float("inf")
    
    def helper(self, c, index, dist):
        
        if index == len(c):
            self.result = min(self.result, max(dist))
            return
        if max(dist) >= self.result:
            return
        
        for i in range(len(dist)):
            dist[i] += c[index]
            self.helper(c, index + 1, dist)
            dist[i] -= c[index]
            
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        self.helper(cookies, 0, [0]*k)
        return self.result
    