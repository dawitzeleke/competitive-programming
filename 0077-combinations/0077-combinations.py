class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb =[]
        def helper(index, path):
            
            if index > n + 1:
                return
            if len(path) == k:
                comb.append(path[:])
                return
            nextpath = path[:]
            nextpath.append(index)
            helper(index+1, path)
            helper(index+1, nextpath)
            
        helper(1,[])
        return comb