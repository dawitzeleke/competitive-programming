class Solution:
    def largestAltitude(self, gains: List[int]) -> int:
        highest = 0

        current_height = 0

        for gain in gains:
            current_height += gain

            highest = max(highest, current_height)

        return highest