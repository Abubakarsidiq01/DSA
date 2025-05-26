from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        lst = []
        for key in dic:
            lst.append(dic[key])
            
        x = max(lst)
        ans = 0
        a = lst.count(x)
        ans = max(ans, a*x)
        return ans

sol = Solution()
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(sol.maxFrequencyElements(nums))

