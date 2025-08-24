class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            total, count = 0, 1 # reset count each time
            for num in nums:
                if total + num > mid:
                    total = 0
                    count += 1
                total += num
            if count <= k: # feasible
                ans = mid
                right = mid - 1
            else:          # not feasible
                left = mid + 1
        return ans
solution = Solution()
print(solution.splitArray([1,2,3,4,5], 2))
solution.splitArray([1,2,3,4,5], 2)
print(solution.splitArray([1,2,3,4,5], 3))
solution.splitArray([1,2,3,4,5], 3)