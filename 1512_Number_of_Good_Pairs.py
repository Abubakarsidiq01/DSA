from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        cnt = Counter()
        for x in nums:
            ans += cnt[x]
            cnt[x] += 1
        return ans

sol = Solution()
nums = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums))

nums = [1,1,1,1]
print(sol.numIdenticalPairs(nums))

