class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    c = board[i][j]

                    # Row check
                    key = f'{c} in row {i}' # same as -> str(c) + ' in row ' + str(i)

                    if key in s:
                        return False
                    else:
                        s.add(key)

                    # Column check
                    key = f'{c} in col {j}' # same as -> str(c) + ' in col ' + str(j)

                    if key in s:
                        return False
                    else:
                        s.add(key)

                    # Box check
                    boxIndex = (i // 3) * 3 + (j // 3)
                    key = f'{c} in box {boxIndex}' # same as -> str(c) + ' in box ' + str(boxIndex)

                    if key in s:
                        return False
                    else:
                        s.add(key) 

        return True