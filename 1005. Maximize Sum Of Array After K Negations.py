import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, -smallest)
        return sum(nums)
"""
nums.sort()
for i in range(k):
    print(nums[0])
    nums[0] *= -1
    nums.sort()
return sum(nums)
"""
sol = Solution()
print(sol.largestSumAfterKNegations([4,2,3], 1))