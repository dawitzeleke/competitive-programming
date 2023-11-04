class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[n - 1]

        for i in range(1, n - 1):
            x, y = coordinates[i]

            if (y - y1) * (x - x2) != (y - y2) * (x - x1):
                return False

        return True