class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - x > k:
                ans += 1
                x = nums[i]
        return ans
solution = Solution()
print(solution.partitionArray([3,6,1,1,6], 3))
print(solution.partitionArray([1,2,3], 1))
print(solution.partitionArray([2,2,4,5], 0))
print(solution.partitionArray([1,2,3,4,5], 1))
print(solution.partitionArray([1,2,3,4,5], 2))
print(solution.partitionArray([1,2,3,4,5], 3))
print(solution.partitionArray([1,2,3,4,5], 4))
print(solution.partitionArray([1,2,3,4,5], 5))