class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        heap = []
        for i in range(row):
            for j in range(col):
                heap.append(matrix[i][j])
                
        heapify(heap)
        k -= 1
        while k > 0:
            k -= 1
            heappop(heap)
            
        return heappop(heap)