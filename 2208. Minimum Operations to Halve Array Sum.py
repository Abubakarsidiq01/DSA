import heapq
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)

        count = 0
        while target > 0:
            x = heapq.heappop(heap)
            target += x/2
            heapq.heappush(heap, x/2)
            count += 1
        return count
sol = Solution()
print(sol.halveArray([5, 19, 8, 1]))
print(sol.halveArray([3, 8, 20]))
print(sol.halveArray([1, 2, 3, 4, 5]))
print(sol.halveArray([1, 1, 1, 1, 1]))
print(sol.halveArray([1, 1, 1, 1, 1]))