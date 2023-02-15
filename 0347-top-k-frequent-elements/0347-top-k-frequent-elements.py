class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d : 
                d[num] += 1
            else:
                d[num] = 1
        sorted_d = sorted(d.items(), key=lambda x:x[1], reverse = True)
        con_d = dict(sorted_d)
        res = []
        list_of_the_keys = list(con_d.keys())
        for i in range (k):
            res.append(list_of_the_keys[i])
        return res   
            