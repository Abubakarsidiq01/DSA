from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        dic = Counter(arr)
        ans  = -1
        for key, value in dic.items():
            if key == value:
                ans = max(ans, key)
        return ans    

sol = Solution()
print(sol.findLucky([2,2,3,4]))
print(sol.findLucky([1,2,2,3,3,3]))
print(sol.findLucky([2,2,2,3,3]))
print(sol.findLucky([5]))
print(sol.findLucky([7,7,7,7,7,7,7]))