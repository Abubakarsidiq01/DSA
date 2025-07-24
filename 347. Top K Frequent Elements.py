import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = defaultdict(int)
        heap = []
        for num in nums:
            dic[num] += 1
        for key, value in dic.items():
            heapq.heappush(heap, (value, key)) # push frequency first since i want to sort by frequecy not by key itself
            if len(heap) > k:
                heapq.heappop(heap)
        return [heaps[1] for heaps in heap]


"""
dic = defaultdict(int)
for num in nums:
    dic[num] += 1
dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
return [key for key, value in dic[:k]]
"""
sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent([1], 1))
print(sol.topKFrequent([1, 2], 2))
print(sol.topKFrequent([1, 2, 3, 4, 5], 3))
print(sol.topKFrequent([1, 2, 3, 4, 5], 4))
print(sol.topKFrequent([1, 2, 3, 4, 5], 5))
print(sol.topKFrequent([1, 2, 3, 4, 5], 6))
print(sol.topKFrequent([1, 2, 3, 4, 5], 7))