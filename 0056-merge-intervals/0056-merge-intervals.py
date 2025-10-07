class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based on their start value

        intervals.sort()

        answer = []

        # iterate over the intervals and check the conflicting ones

        for interval in intervals:
            if answer:
                start, end = answer[-1]

                curr_start = interval[0]
                curr_end = interval[1]

                if end >= curr_start:
                    answer.pop()
                    answer.append([start, max(end, curr_end)])
                else:
                    answer.append(interval)

            else:
                answer.append(interval)

        return answer