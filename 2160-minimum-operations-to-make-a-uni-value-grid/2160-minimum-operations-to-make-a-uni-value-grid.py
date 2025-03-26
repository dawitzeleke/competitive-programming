class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total_amount = len(grid) * len(grid[0])
        min_num = max_num = grid[0][0]
        for row in grid:
            for num in row:
                min_num = min(min_num, num)
                max_num = max(max_num, num)
        
        left = min_num
        right = max_num
        pivot = None
        while left <= right:
            poss_pivot = (left + right) // 2
            less, equal, more = 0, 0, 0
            for row in grid:
                for num in row:
                    if num < poss_pivot:
                        less += 1
                    elif num == poss_pivot:
                        equal += 1
                    else:
                        more += 1
            if not equal:
                if more <= total_amount // 2:
                    right = poss_pivot - 1
                else:
                    left = poss_pivot + 1
                continue
            if less == more:
                pivot = poss_pivot
                break
            if less > more:
                if more + equal >= (total_amount + 1) // 2:
                    pivot = poss_pivot
                    break
                right = poss_pivot - 1
            else:
                if less + equal >= (total_amount + 1) // 2:
                    pivot = poss_pivot
                    break
                left = poss_pivot + 1

        res = 0
        for row in grid:
            for num in row:
                diff = abs(num - pivot)
                if diff % x:
                    return -1
                res += diff // x
        return res 