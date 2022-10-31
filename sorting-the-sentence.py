class Solution(object):
    def sortSentence(self, s):
        temp= s.split()
        word={}
        ans=''
        for i in temp:
            word[i[-1]]= i[:-1]
        for i in sorted(word):
            ans=ans+''.join(word[i])+' '
        ans=ans[:-1]
        return ans
