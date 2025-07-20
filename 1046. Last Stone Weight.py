import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = abs(heapq.heappop(heap))
            second = abs(heapq.heappop(heap))

            if first != second:
                heapq.heappush(heap, -abs(first - second))
        return -heap[0] if heap else 0
sol = Solution()
print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(sol.lastStoneWeight([1]))
print(sol.lastStoneWeight([1, 1]))
print(sol.lastStoneWeight([1, 2]))
print(sol.lastStoneWeight([1, 2, 3]))
print(sol.lastStoneWeight([1, 2, 3, 4]))
print(sol.lastStoneWeight([1, 2, 3, 4, 5]))