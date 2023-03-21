class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  
        d = {0:1}
        
        current_sum = 0
        answer = 0
        for num in nums:
            current_sum += num
            if current_sum - k in d:
                answer += d[current_sum - k]
            if current_sum not in d:
                d[current_sum] = 1
            else:
                d[current_sum] += 1
        return answer