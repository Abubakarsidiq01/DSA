class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        while n != 1:
            if n % 2 != 0: return False
            n = n // 2
        return True
        """
        def backtrack(curr):
            if curr <= 0:
                return False
            if curr == 1:
                return True
            if curr % 2 != 0:
                return False
            return backtrack(curr // 2)
        return backtrack(n)
        """
solution = Solution()
print(solution.isPowerOfTwo(1))
solution.isPowerOfTwo(1)
print(solution.isPowerOfTwo(16))
solution.isPowerOfTwo(16)
print(solution.isPowerOfTwo(3))
solution.isPowerOfTwo(3)
print(solution.isPowerOfTwo(4))
solution.isPowerOfTwo(4)
print(solution.isPowerOfTwo(5))