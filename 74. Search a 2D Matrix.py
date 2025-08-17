class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m*n) -1

        while left <= right:
            mid = (left + right)//2
            row = mid // n
            col = mid % n
            num = matrix[row][col]

            if num == target:
                return num
            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        """
        for row in matrix:
            for num in row:
                if num == target:
                    return True
        return False

        OR
        for row in matrix:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        """
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))