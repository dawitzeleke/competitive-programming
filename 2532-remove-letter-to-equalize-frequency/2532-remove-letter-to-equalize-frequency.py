from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        lettercount = Counter(word)
        

        for char in word:
            lettercount[char] -= 1

            if lettercount[char] == 0:
                del lettercount[char]
            if len(set(lettercount.values())) == 1:
                return True

            if char in lettercount:
                lettercount[char] += 1
            else:
                lettercount[char] = 1


        return False

        

        