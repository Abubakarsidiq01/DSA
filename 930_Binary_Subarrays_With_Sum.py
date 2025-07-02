from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # to count subarrays that start from index 0

        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num
            ans += count[prefix_sum - goal]  # check if prefix_sum - goal was seen before
            count[prefix_sum] += 1

        return ans
solution = Solution()
print(solution.numSubarraysWithSum([1,0,1,0,1], 2))
print(solution.numSubarraysWithSum([0,0,0,0,0], 0))