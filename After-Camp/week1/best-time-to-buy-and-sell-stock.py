class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        current_max = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else :
                current_max = max(current_max, prices[r]-prices[l])
                r += 1
        return current_max