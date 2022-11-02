class Solution(object):
    def findOriginalArray(self, changed):
        result= []
        n= len(changed)
        if (n%2)!=0:
            return []
        else:
            for i in range (len(changed)):
                for j in range (i+1, len(changed)):
                    if 2*changed[i]==(changed[j]):
                        result.append(changed[i])  
            return result  
