class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []

        for a, b in costs:
            difference.append([b - a, a, b])
        difference.sort()

        answer = 0

        for i in range(len(costs) // 2):
            answer += difference[i][2]

        for j in range(len(costs) // 2, len(costs)):
            answer += difference[j][1]


        return answer