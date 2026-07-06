class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        merge = []

        intervals.sort(key=lambda x: (x[0], -x[1]))

        for interval in intervals:
            if not merge:
                merge.append(interval)

            else:
                temp = merge[-1]
                if temp[0] <= interval[0] and temp[1] >= interval[1] :
                    continue
                
                else:
                    merge.append(interval)


        return len(merge)