class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans=[]
        c=1
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                c+=1
            else:
                ans.append(c)
                c=1
        ans.append(c)
        res=0
        for i in range(0,len(ans)-1):
            res+=min(ans[i],ans[i+1])
        return res