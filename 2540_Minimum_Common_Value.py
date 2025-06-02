from collections import defaultdict
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        """
        dic = defaultdict(int)
        for num in nums1 + nums2:
            dic[num] += 1
        ans = []
        for key in dic:
            if dic[key] >= 2:
                ans.append(dic[key])
        return min(ans) if len(ans) > 0 else -1
        """
        check = set(nums1)
        ans = []
        for num in nums2:
            if num in check:
                ans.append(num)
        return min(ans) if len(ans) > 0 else -1 

sol = Solution()
nums1 = [1,2,3]
nums2 = [2,4]
print(sol.getCommon(nums1, nums2))
