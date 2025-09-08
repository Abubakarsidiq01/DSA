class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        for num in nums:
            temp_ans = []
            for element in ans:
                temp_ans.append(element + [num])
            ans.extend(temp_ans)
        return ans
sol = Solution()
print(sol.subsets([1,2,3]))
print(sol.subsets([0]))
"""
ans = []
def backtrack(curr, i):
    if i > len(nums):
        return
    ans.append(curr[:])
    for j in range(i, len(nums)):
        curr.append(nums[j])
        backtrack(curr, j + 1)
        curr.pop()

backtrack([], 0)
return ans
"""