# Binary search problme
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # dimensions of matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        if not matrix or not matrix[0]:
            return False

        # start from the top right corner
        row = 0
        col = COLS - 1

        # move until we either find a target or go out of bounds
        while row < ROWS and col >= 0:
            if matrix[row][col] == target:
                # found the target so output ture
                return True
            elif matrix[row][col] > target:
                # current value to big so move left
                col -= 1
            else:
                # current value to small so move down
                row += 1

        # target not found
        return False