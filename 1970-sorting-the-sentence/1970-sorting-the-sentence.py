class Solution:
    def sortSentence(self, s: str) -> str:
        s_array = s.split(" ")

        for i, word in enumerate(s_array):
            order = int(word[-1])
            word = word[:len(word) - 1]
            s_array[i] = (order, word[:len(word)])
        
        s_array.sort()
        answer = s_array[0][1]

        for order, word in s_array[1:]:
            answer = answer + " " + word 

        return answer

