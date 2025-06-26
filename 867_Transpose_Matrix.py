class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transposed = []
        row = len(matrix)
        col = len(matrix[0])
        for j in range(col):
            new_row = [] #creates a fresh empty list each time (one for each column.)
            for i in range(row):
                new_row.append(matrix[i][j])
            transposed.append(new_row)
        return transposed
solution = Solution()
print(solution.transpose([[1,2,3],[4,5,6],[7,8,9]]))