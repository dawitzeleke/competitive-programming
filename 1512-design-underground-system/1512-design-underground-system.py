class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}
        self.totalTime = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = [stationName, t]


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkedin = self.checkedIn[id]
        start = checkedin[0]
        time = checkedin[1]
        timediff = t - time
        if (start, stationName) not in self.totalTime:
            self.totalTime[(start, stationName)] = [timediff, 1]
        else:
            self.totalTime[(start, stationName)][0] += timediff
            self.totalTime[(start, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totaltime = self.totalTime[(startStation, endStation)][0]
        totalcount = self.totalTime[(startStation, endStation)][1]
        return totaltime / totalcount


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)