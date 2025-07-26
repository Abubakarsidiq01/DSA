from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dic = Counter(words)
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, (-value, key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


s = Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))