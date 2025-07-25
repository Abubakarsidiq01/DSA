import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        x1 = y1 = 0
        
        heap = []
        heapq.heapify(heap)
        
        for x2, y2 in points:
            distance = ((x1 - x2)**2) + ((y1 - y2)**2)
            heapq.heappush(heap, (-distance, [x2, y2]))
            
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
sol = Solution()
print(sol.kClosest([[1, 3], [-2, 2]], 1))
print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
print(sol.kClosest([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 3))
print(sol.kClosest([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 4))
print(sol.kClosest([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 5))
print(sol.kClosest([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 6))
print(sol.kClosest([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 7))