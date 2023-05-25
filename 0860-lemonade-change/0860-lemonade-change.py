class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fivebills = 0
        tenbills = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                fivebills += 1
            elif bills[i] == 10:
                
                if not fivebills:
                    return False
                tenbills += 1
                fivebills -= 1
            else:
                
                if fivebills == 0 or fivebills < 3 and not tenbills:
                    return False
                if tenbills:
                    tenbills -= 1
                    fivebills -= 1
                else:
                    fivebills -= 3
                    
        return True