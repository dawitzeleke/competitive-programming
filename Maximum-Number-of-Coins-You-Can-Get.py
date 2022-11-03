class Solution(object):
    def maxCoins(self, piles):
        
        piles.sort()
        result = 0
        n = len(piles)
        for i in range(len(piles)//3):
            result += piles[n-(i+1)*2]
        return result
