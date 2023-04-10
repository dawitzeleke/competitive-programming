import math
from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        fre = count.values()
        GCD = math.gcd(*fre)
        
        if GCD >= 2:
            return True
        else:
            return False
        