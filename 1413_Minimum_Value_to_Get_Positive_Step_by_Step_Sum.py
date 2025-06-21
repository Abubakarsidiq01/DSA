class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        min_value, total = 0, 0
        for num in nums:
            total += num
            min_value = min(min_value, total)
        return 1 - min_value

solution = Solution()
print(solution.minStartValue([-3,2,-3,4,2]))
