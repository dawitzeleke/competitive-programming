class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def rev_invert(s):
    
            temp = list(s)
            for i in range (len(temp)):
                if temp[i] == "1":
                    temp[i] = "0"
                else:
                    temp[i] = "1"
            return "".join(temp)
        
        def helper(n):
            
            if n == 1:
                return "0"
            x = helper(n-1)
            return x + "1" + rev_invert(x)[::-1]
        y = helper(n)
        # print(y)
        return y[k-1]
       
                    
            
        
        
        
        