class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degree_per_hour = 30
        degree_per_min = 6
        hour_degree = (hour + (minutes/60)) * 30
        minute_degree = minutes * 6

        clock_wise = abs(minute_degree - hour_degree)
        anti_clockwise = abs(360 - clock_wise)
        answer = min(clock_wise, anti_clockwise)

        return answer