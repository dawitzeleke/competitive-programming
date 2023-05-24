class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = 0
        while k > 0:
            k -= 1
            if numOnes > 0:
                answer += 1
                numOnes -= 1
            elif numZeros > 0:
                numZeros -= 1
            else:
                answer -= 1
                numNegOnes -= 1
                
        return answer