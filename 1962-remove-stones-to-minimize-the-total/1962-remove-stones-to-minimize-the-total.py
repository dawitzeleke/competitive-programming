import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [ -x for x in piles]
        heapify(heap)
        while k > 0:
            k -= 1
            temp = - heappop(heap)
            heappush(heap, - math.ceil(temp / 2))
        total = 0
        for num in heap:
            total += (-num)
        return total