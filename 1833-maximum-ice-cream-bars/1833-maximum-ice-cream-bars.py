class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        remaining_coins = coins
        bars = 0
        costs.sort()

        for cost in costs:
            if cost > remaining_coins:
                break
            bars += 1
            remaining_coins -= cost
        return  bars
        