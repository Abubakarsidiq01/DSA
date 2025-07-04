class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        a = sum(nums)
        b = count = 0
        for i in range(len(nums)-1):
            b += nums[i]
            if b >= (a-b):
                count += 1
        return count
solution = Solution()
print(solution.waysToSplitArray([10,4,-8,7]))
print(solution.waysToSplitArray([2,3,1,0]))

"""
count = 0
for i in range(1, len(nums)):
    if sum(nums[:i]) >= sum(nums[i:]):
        count += 1
return count
"""