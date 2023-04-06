class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(len(edges)):
            for num in edges[i]:
                if num in edges[i + 1]:
                    return num