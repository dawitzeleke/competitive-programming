class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        target_index = 0

        for i in range(1, n + 1):
            if target_index >= len(target):
                break
            answer.append("Push")

            if i == target[target_index]:
                target_index += 1

            else:
                answer.append("Pop")
            
        return answer