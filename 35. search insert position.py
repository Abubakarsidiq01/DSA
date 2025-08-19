class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= target:
                right = mid -1
            else:
                left = mid +1
        return left
solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))
solution.searchInsert([1,3,5,6], 2)
print(solution.searchInsert([1,3,5,6], 7))
solution.searchInsert([1,3,5,6], 0)
print(solution.searchInsert([1,3,5,6], 4))
solution.searchInsert([1,3,5,6], 0)
"""
final = []
final.extend(nums)
final.append(target)

final.sort()

for i in range(len(final)):
    if final[i] == target:
        return i
"""