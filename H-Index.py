class Solution(object):
    def hIndex(self, citations):
        if not citations:
            return 0
        citations.sort()
        h = len(citations)
        if citations[0] >= h:
            return h
        else:
            for i in range(1, len(citations)+1):
                if h <= citations[i-1]:
                    return h
                h -= 1
        return h
