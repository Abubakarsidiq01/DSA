class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b
solution = Solution()
print(solution.fib(2))
solution.fib(2)
print(solution.fib(3))
solution.fib(3)
print(solution.fib(4))
solution.fib(4)
print(solution.fib(5))
solution.fib(5)
print(solution.fib(6))
solution.fib(6)
"""
def f(n):
    if n == 0 or n == 1:
        return n
    return f(n - 1) + f(n - 2)
return f(n)
"""
