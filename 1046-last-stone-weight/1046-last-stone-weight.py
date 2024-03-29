class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -(stone))
            
        while len(heap) > 1:
            first = - (heappop(heap))
            second = - (heappop(heap))
            
            if first == second:
                continue
            if first > second:
                heappush(heap, -(first - second))
                
        if heap:
            return -heap[0]
        else:
            return 0