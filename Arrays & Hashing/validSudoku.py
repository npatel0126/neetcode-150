"""
Idea:
Validate a Sudoku board by ensuring that each row, column, and 3x3 sub-grid contains no duplicate numbers. 
Use hash sets to track seen numbers for each row, column, and 3x3 sub-grid (indexed by `(row // 3, col // 3)`). 
If any number is already present in its corresponding row, column, or sub-grid set, the board is invalid.

Examples:
- Input: A valid 9x9 partially filled Sudoku board -> Output: True
- Input: An invalid board with a duplicate number in a column -> Output: False

Complexity:
- Time: O(1) since the board size is fixed at 9x9 (81 cells total).
- Space: O(1) since the hash sets store at most 81 elements.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # Key = (row // 3, col // 3)

        for row in range(9):
            for col in range(9):
                current_val = board[row][col]
                if current_val == ".":
                    continue 
                
                if (current_val in rows[row] or
                    current_val in cols[col] or
                    current_val in squares[row // 3, col // 3]):
                    return False
                
                cols[col].add(current_val)
                rows[row].add(current_val)
                squares[row // 3, col // 3].add(current_val)
                
        return True
