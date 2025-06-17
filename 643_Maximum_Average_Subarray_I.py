from collections import deque
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        q = deque()
        ans = float('-inf')
        count = 0
        for num in nums:
            q.append(num)
            count += num
            if len(q) >= k:
                mid = count/k
                ans = max(ans, mid)
                count -= q.popleft()
               
        return ans

solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))

solution2 = Solution()
print(solution2.findMaxAverage([1,12,-5,-6,50,3], 4))

"""
ans = float('-inf')
left, right = 0, k - 1

while right < len(nums):
    window_sum = sum(nums[i] for i in range(left, right + 1))
    ans = max(ans, window_sum)
    left += 1
    right += 1

return ans / k
"""
