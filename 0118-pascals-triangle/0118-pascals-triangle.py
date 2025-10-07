class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for row in range(2, numRows + 1):
            prev_row = triangle[-1]
            curr_row = [0] * row
            curr_row[-1] = 1
            curr_row[0] = 1
            for r in range(1, row - 1):

                curr_row[r] = prev_row[r] + prev_row[r - 1]

            triangle.append(curr_row)

        return triangle

                


