class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        num = sorted(set(nums))
        return num[-3] if len(num) >= 3 else num[-1]
s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))
print(s.thirdMax([1, 2, 2, 5, 3, 5]))
print(s.thirdMax([1, 2, 2, 5, 3, 5]))