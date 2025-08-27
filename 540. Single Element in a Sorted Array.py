class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
solution = Solution()
print(solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(solution.singleNonDuplicate([3,3,7,7,10,11,11]))
solution.singleNonDuplicate([3,3,7,7,10,11,11])
print(solution.singleNonDuplicate([1,1,2]))
solution.singleNonDuplicate([1,1,2])
print(solution.singleNonDuplicate([1]))
solution.singleNonDuplicate([1])