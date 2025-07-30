class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid
        
        return True
solution = Solution()
print(solution.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))
print(solution.asteroidsDestroyed(5, [4, 9, 19, 5, 21]))
print(solution.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))
print(solution.asteroidsDestroyed(10, [3, 9, 19, 5, 21]))