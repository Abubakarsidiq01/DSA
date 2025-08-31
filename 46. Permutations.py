class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans
        """

        ans = [[]]
        for num in nums:
            curr = []
            for lst in ans:
                for i in range(len(lst)+1):
                    curr.append(lst[:i] + [num] + lst[i:])
            ans = curr
        return ans
solution = Solution()
print(solution.permute([1,2,3]))
solution.permute([1,2,3])
print(solution.permute([0,1]))
solution.permute([0,1])
print(solution.permute([1]))
solution.permute([1])