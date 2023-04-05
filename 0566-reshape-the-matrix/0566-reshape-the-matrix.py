class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        answer = []
        h = v = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(mat[v][h])
                h += 1
                if h == len(mat[0]):
                    h = 0
                    v += 1
            answer.append(temp)
            
            
        return answer
            