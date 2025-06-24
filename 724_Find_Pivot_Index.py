class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftsum = 0

        for i in range(len(nums)):
            # At each index i, the right side sum is total - left_sum - nums[i]
            rightsum = total - leftsum - nums[i] 
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1
    
solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6]))

"""
for i in range (len(nums)):
    if sum(nums[:i]) == sum(nums[i+1:]):
        return i
return -1
"""