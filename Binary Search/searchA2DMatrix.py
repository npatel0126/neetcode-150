"""
Idea:
Perform a two-step binary search. First, use binary search on the rows to find the candidate row 
where the target falls between the row's first and last elements. Once the correct row is identified, 
perform a second binary search within that specific row to locate the target value.

Examples:
- Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3 -> Output: True
- Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13 -> Output: False

Complexity:
- Time: O(log M + log N) = O(log(M * N)), where M is the number of rows and N is the number of columns.
- Space: O(1) using only constant extra space for pointers.
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, bot_row = 0, ROWS - 1
        while top_row <= bot_row:
            row = (top_row + bot_row) // 2
            if target > matrix[row][-1]:
                top_row = row + 1
            elif target < matrix[row][0]:
                bot_row = row - 1
            else:
                break 
        
        if not (top_row <= bot_row):
            return False

        row = (top_row + bot_row) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target >  matrix[row][mid]:
                l = mid + 1
            elif target <  matrix[row][mid]:
                r = mid - 1
            else: 
                return True
        return False
