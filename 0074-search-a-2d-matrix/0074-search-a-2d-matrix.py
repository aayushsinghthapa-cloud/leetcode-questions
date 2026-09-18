# In this question, we treat the 2D sorted array as a 1D array because of the constraints given.

class Solution(object):
    def searchMatrix(self, matrix, target):
        # We first assign number of rows, and columns present in the matrix to m, n
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1

        # We go till both the pointers meet at a common point
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n # '% n' gives the positions inside the row

            val = matrix[row][col]

            if (val == target):
                return True
            elif (val > target):
                right = mid - 1
            else:
                left = mid + 1
        return False