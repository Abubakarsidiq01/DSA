import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [num for num in nums]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return heapq.heappop(heap)
sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(sol.findKthLargest([1], 1))
print(sol.findKthLargest([1, 2], 2))
print(sol.findKthLargest([1, 2, 3, 4, 5], 3))
print(sol.findKthLargest([1, 2, 3, 4, 5], 4))
print(sol.findKthLargest([1, 2, 3, 4, 5], 5))
print(sol.findKthLargest([1, 2, 3, 4, 5], 6))