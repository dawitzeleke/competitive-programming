class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime: list[bool] = [True for _ in range(0, right + 1)]
        is_prime[0] = is_prime[1] = False

        i = 2

        while i * i <= right:
            if is_prime[i]:
                j = i * i
                while j <= right:
                    is_prime[j] = False
                    j += i
            i += 1
            
    
        temp = []
        
        for i, bol in enumerate(is_prime):
            if bol and i >= left:
                temp.append(i)
        print(temp)
        if len(temp) < 2:
            return [-1, -1]
        result = [0, 0]
        min_diff = float("inf")
        l = 0
        for r in range(1, len(temp) ):
            if temp[r] - temp[l] < min_diff:
                min_diff = temp[r] - temp[l]
                result[0] = temp[l]
                result[1] = temp[r]
                
            l += 1
            r += 1
                
                
        return result