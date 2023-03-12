class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        GCF = 1 if n%2 == 1 else 2
        
        return (n*2)//GCF