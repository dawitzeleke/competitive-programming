class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        left = 0 
        right = 0
        max_fruit = 0
        while right < len(fruits):
            if fruits[right] not in d:
                d[fruits[right]] = 1
            else:
                d[fruits[right]] += 1
            
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
            max_fruit = max(max_fruit, right - left + 1)
            right += 1
        return max_fruit