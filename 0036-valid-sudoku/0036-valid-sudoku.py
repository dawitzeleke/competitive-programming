class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    c = board[i][j]

                   
                    key = f'{c} in row {i}' 

                    if key in s:
                        return False
                    else:
                        s.add(key)


                    key = f'{c} in col {j}' 

                    if key in s:
                        return False
                    else:
                        s.add(key)

                   
                    boxIndex = (i // 3) * 3 + (j // 3)
                    key = f'{c} in box {boxIndex}' 

                    if key in s:
                        return False
                    else:
                        s.add(key) 

        return True