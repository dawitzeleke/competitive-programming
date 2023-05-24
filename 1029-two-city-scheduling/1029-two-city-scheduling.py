class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n =  len(costs)
        total = 0
        diff = [a - b for a, b in costs]
        helper = [(dif, i) for i, dif in enumerate(diff)]
        helper.sort(key=lambda x: x[0])
        count = 0
        
        for dif, i in helper:
            
            if count < n / 2:
                total += costs[i][0]
            if count >= n / 2:
                total += costs[i][1]
                
                
            count += 1
            
        return total 
            