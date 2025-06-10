from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        queue = deque()
        for i in range(len(nums)):
            # maintain monotonic decreasing.
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()
            
            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums, k))

nums = [1]
k = 1
print(sol.maxSlidingWindow(nums, k))

nums = [1,-1]
k = 1
print(sol.maxSlidingWindow(nums, k))



"""
x = 0
y = k
lst1 = []
lst2 = []

for i in range(len(nums) - k+1):  # include last window
    for j in range(x, y):
        lst1.append(nums[j])
    a = max(lst1)
    lst2.append(a)
    x += 1
    y += 1
    lst1 = []

return lst2
"""
