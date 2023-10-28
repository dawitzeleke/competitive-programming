class DetectSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.points = []
    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1
        self.points.append(point)
    def count(self, point: List[int]) -> int:

        squareCounts = 0
        for x, y in self.points:
            if abs(x - point[0]) != abs(y - point[1]) or x == point[0] or y == point[1]:
                continue
            squareCounts += self.pointCount[(x, point[1])] * self.pointCount[(point[0], y)]
 
        return squareCounts
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)