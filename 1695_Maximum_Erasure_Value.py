from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = total = ans = 0
        dic = defaultdict(int)

        for right in range(len(nums)):
            dic[nums[right]] += 1
            total += nums[right]
            while dic[nums[right]] != 1 and left < right:
                total -= nums[left] 
                dic[nums[left]] -= 1
                left += 1
            ans = max(ans, total)   
        return ans
solution = Solution()
print(solution.maximumUniqueSubarray([4,2,4,5,6]))
print(solution.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))