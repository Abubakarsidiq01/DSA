from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        dic = Counter(arr)
        sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1]))
        for key, value in sorted_dic.items():
            if k >= value:
                k -= value
                dic[key] = 0
            else:
                break
        count = 0
        for val in dic.values():
            if val > 0:
                count += 1
        return count
s = Solution()
print(s.findLeastNumOfUniqueInts([5, 7, 3, 3, 2, 2, 2, 2], 3))
print(s.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2, 4, 1, 2], 3))
print(s.findLeastNumOfUniqueInts([1, 2, 3, 4, 5], 2))
print(s.findLeastNumOfUniqueInts([1, 2, 3, 4, 5], 3))
print(s.findLeastNumOfUniqueInts([1, 2, 3, 4, 5], 4))
print(s.findLeastNumOfUniqueInts([1, 2, 3, 4, 5], 5))
print(s.findLeastNumOfUniqueInts([1, 2, 3, 4, 5], 6))
print(s.findLeastNumOfUniqueInts([1, 2, 3, 4, 5], 7))