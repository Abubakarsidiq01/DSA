from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dic = Counter(arr)
        return len(set(dic.values())) == len(dic)
solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
print(solution.uniqueOccurrences([1,2]))
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))