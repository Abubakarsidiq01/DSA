class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[-1] + nums[i])
        return ans

solution = Solution()
print(solution.runningSum([1,2,3,4]))
