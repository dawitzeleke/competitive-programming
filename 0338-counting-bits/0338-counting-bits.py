class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            counter = 0
            while i > 0:
                counter += i & 1
                i >>= 1
            answer.append(counter)
        return answer