from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        temp = [values for key, values in freq.items()]
        unique = set(temp)

        return len(temp) == len(unique)

