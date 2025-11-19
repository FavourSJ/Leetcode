# Binary search problme
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        row, col = 0, COLS - 1  # Start from the top-right corner

        # Move until we either find the target or go out of bounds
        while row < ROWS and col >= 0:
            if matrix[row][col] == target:
                return True       # Found the target
            elif matrix[row][col] > target:
                col -= 1          # Current value too large, move left
            else:
                row += 1          # Current value too small, move down

        return False               # Target not found