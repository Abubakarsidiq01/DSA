from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        ans = 0
        for key in seen:
            if seen[key] == 1:
                ans += key
        return ans

        
sol = Solution()
nums = [1,2,3,2]
print(sol.sumOfUnique(nums))

nums = [1,1,1,1,1]
print(sol.sumOfUnique(nums))

nums = [1,2,3,4,5]
print(sol.sumOfUnique(nums))


