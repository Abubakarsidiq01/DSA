class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        curr = 0
        left = 0
        answer = float("inf")
        for right in range(len(nums)):
            curr += nums[right]    
            while curr >= target:
                answer = min(answer, right - left + 1)
                curr -= nums[left]
                left += 1
        return 0 if answer == float('inf') else answer

solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))
