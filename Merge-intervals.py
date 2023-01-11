class Solution(object):
    def merge(self, intervals):
        intervals.sort( key = lambda i: i[0])
        result = [intervals[0]]
        for start , end in intervals[1:]:
            lastend = result[-1][1]
            if lastend >= start:
                result[-1][1] = max (lastend, end)
            else:
                result.append([start,end])

        return result
