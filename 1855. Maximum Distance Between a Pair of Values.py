class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        num1 = 0
        num2 = 0
        ans = 0
        while num1 < len(nums1) and num2 < len(nums2):
            if num1 <= num2 and nums1[num1] <= nums2[num2]:
                ans = max(ans, num2 - num1)
                num2 += 1
            elif num1 <= num2 and nums1[num1] >= nums2[num2]:
                num1 += 1
            elif num1 > num2:
                num2 += 1
        return ans

solution = Solution()
print(solution.maxDistance([55,30,5,4,2], [100,20,10,10,5]))
solution.maxDistance([55,30,5,4,2], [100,20,10,10,5])
print(solution.maxDistance([2,2,2], [10,10,1]))
solution.maxDistance([2,2,2], [10,10,1])
print(solution.maxDistance([30,29,19,5], [25,25,25,25,25]))
solution.maxDistance([30,29,19,5], [25,25,25,25,25])
        
"""
The cleaner code but the first one was what i thought about first.

ans = 0
i = j = 0

while i < len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        ans = max(ans, j - i)
        j += 1
    else:
        i += 1
return ans

Why we don’t need to explicitly check i <= j
At the start: both i = 0 and j = 0, so i ≤ j is true.
In the loop:
If nums1[i] <= nums2[j], then we use this pair, record j - i, and increase j.
This increases j only, so j will never fall behind i.
If nums1[i] > nums2[j], then we increase i.
This might make i catch up to j, but never go past it by more than 1 step before j moves again.
Because if i gets larger than j, the condition nums1[i] <= nums2[j] can’t be satisfied yet, so we’ll just keep moving i forward until the inequality works again.
In other words, the algorithm implicitly enforces i ≤ j by how it moves the pointers:
j only moves forward when the pair is valid.
i only moves forward when the pair is invalid.
So at the moment we actually use j - i, we are guaranteed i ≤ j.
"""

"""
not the best solution but it works
ans = 0
for i in range(len(nums1)):
    j = i
    while j < len(nums2) and i <= j and nums1[i] <= nums2[j]:
        ans = max(ans, j - i)
        j += 1
return ans 
"""
