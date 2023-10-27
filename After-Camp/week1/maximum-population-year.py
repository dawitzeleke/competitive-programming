class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        temp = [0] * 3000
        for i in range(len(logs)):
            temp[logs[i][0]] += 1
            temp[logs[i][1]] -= 1
        maxPopulation = -float("inf")
        maxYear = 0
        for i in range(1950, 2051):
            temp[i] += temp[i - 1]
            if temp[i] > maxPopulation:
                maxPopulation = temp[i]
                maxYear = i

        return maxYear

        
