class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        Wcount = 0
        
        for i in range(k):
            if blocks[i] == "W":
                Wcount += 1
        minimum = Wcount
        
        left = 1
        right = k

        while right < len(blocks):
            

            if blocks[left - 1] == "W":
                Wcount -= 1

            if blocks[right] == "W":
                Wcount += 1
            minimum = min(minimum, Wcount)

            left += 1
            right += 1

        return minimum


        
