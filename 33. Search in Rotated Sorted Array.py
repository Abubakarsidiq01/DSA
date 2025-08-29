class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # Left side is sorted
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))
solution.search([4,5,6,7,0,1,2], 0)
print(solution.search([4,5,6,7,0,1,2], 3))
solution.search([4,5,6,7,0,1,2], 3)
print(solution.search([1], 0))
solution.search([1], 0)
print(solution.search([1], 1))
solution.search([1], 1)