class Solution(object):
    def minSetSize(self, arr):
        freq_dic={}
        for num in arr:
            if num in freq_dic:
                freq_dic[num]+=1
            else:
                freq_dic[num]=1
        sorted_list = sorted(freq_dic.values(), reverse= True)               
        half= len(arr)//2
        n= len(arr)
        picked= 0
        for num in sorted_list:
            if n> half:
                n-=num
                picked+=1
            else:
                break
        return picked
