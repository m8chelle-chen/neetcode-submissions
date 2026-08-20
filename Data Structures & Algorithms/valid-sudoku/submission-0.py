class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for r in range(len(board)):
            for c in range(len(board[r])):
                box_index = (r//3)*3 + (c//3)
                digit = board[r][c] 
                if(digit == '.'):
                    continue
                if(digit in row[r] or digit in col[c] or digit in boxes[box_index]):
                    return False

                row[r].add(digit)
                col[c].add(digit)
                boxes[box_index].add(digit)

        return True


