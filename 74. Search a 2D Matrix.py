class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            for num in row:
                if num == target:
                    return True
        return False
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))