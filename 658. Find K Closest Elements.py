import heapq
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        heap = []
        for num in arr:
            distance = abs(x-num)
            heapq.heappush(heap, (-distance, -num))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted([-pair[1] for pair in heap])