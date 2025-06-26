class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        x = len(mat)
        total = 0
        for i in range (x):
            # add the main diagonal and anti-diagonal 
            total += mat[i][i] + mat[i][x-i-1]
            
        # If n is odd, remove the middle element (it was added twice)
        if x % 2 == 1:
            middle = mat[x//2][x//2]
            total -= middle
        return total
    
solution = Solution()
print(solution.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))