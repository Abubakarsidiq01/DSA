class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height) - 1
        left = 0
        right = len(height) - 1
        count = 0
        while left < right:
            a = min(height[left], height[right])
            count = max(count, (n * a))
            if height and height[left] < height[right]:
                left += 1
            else:
                right -= 1
            n -= 1
        return count
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))