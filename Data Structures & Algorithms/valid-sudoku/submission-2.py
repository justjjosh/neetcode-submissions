class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #rows, cols, and square to store our numbers
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                number = board[r][c]
                if number == ".":
                    continue
                if number in rows[r] or number in cols[c] or number in square[r//3, c//3]:
                    return False
                else:
                    rows[r].add(number)
                    cols[c].add(number)
                    square[r//3, c//3].add(number)
        return True