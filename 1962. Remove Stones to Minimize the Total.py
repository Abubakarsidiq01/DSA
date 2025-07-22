import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        for i in range(k):
            max_num = heapq.heappop(piles)
            heapq.heappush(piles, max_num//2)
        return -(sum(piles))

sol = Solution()
print(sol.minStoneSum([5, 4, 9], 2))
print(sol.minStoneSum([4, 3, 6, 7], 3))
print(sol.minStoneSum([1, 2, 3, 4, 5], 4))
print(sol.minStoneSum([1, 2, 3, 4, 5], 5))
print(sol.minStoneSum([1, 2, 3, 4, 5], 6))
print(sol.minStoneSum([1, 2, 3, 4, 5], 7))