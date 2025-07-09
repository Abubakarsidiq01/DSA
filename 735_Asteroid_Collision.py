class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:    # Top of stack explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a: # Both explode
                    stack.pop()
                break
            else:
                stack.append(a)

        return stack

sol = Solution()
print(sol.asteroidCollision([5, 10, -5]))
print(sol.asteroidCollision([8, -8]))
print(sol.asteroidCollision([10, 2, -5]))
print(sol.asteroidCollision([-2, -1, 1, 2]))
print(sol.asteroidCollision([-2, -2, 1, -2]))
print(sol.asteroidCollision([-2, 1, -2, -2]))
print(sol.asteroidCollision([1, -2, -2, -2]))
print(sol.asteroidCollision([1, 2, 3, 4, 5]))