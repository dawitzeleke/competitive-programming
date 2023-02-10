class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m=sum(cardPoints[:k])
        s=sum(cardPoints[:k])
        cnt=k-1
        for i in range(1,k+1):
            s=s-cardPoints[cnt]+cardPoints[-i]
            cnt-=1
            m=max(m,s)
        return m