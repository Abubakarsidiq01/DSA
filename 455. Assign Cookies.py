class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        while s and g:
            if s[-1] >= g[-1]:
                count += 1
                s.pop()
            g.pop()
        return count
sol = Solution()
print(sol.findContentChildren([1,2,3], [1,1]))
print(sol.findContentChildren([1,2,3], [1,1]))