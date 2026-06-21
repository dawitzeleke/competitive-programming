class Solution:
    def maxDistance(self, moves: str) -> int:
        y_dist = 0
        x_dist = 0
        man_dist = 0
        for move in moves:

            if move == "U":
                y_dist += 1
            elif move == "D":
                y_dist -= 1 
            elif move == "R":
                x_dist += 1
            elif move == "L":
                x_dist -= 1 
            else:
                man_dist += 1

        return man_dist + abs(y_dist) + abs(x_dist)
        