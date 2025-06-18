class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        curr = 1
        answer = 0

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            answer += right - left + 1
        return answer

solution = Solution()
print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))

"""
If you don’t add if k <= 1: return 0, and k = 0 or k = 1,
your while curr >= k: loop will never stop →
It'll keep shrinking until left > right → then nums[left] crashes → IndexError.
"""