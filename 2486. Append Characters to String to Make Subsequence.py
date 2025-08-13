class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left = 0
        right = 0

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                right += 1
            left += 1
        return len(t) - right
sol = Solution()
print(sol.appendCharacters("coaching", "coding"))

"""
wrong solution but ran the three testcases
ans = []
left = 0
right = 0
total = 0
count = 0

while right < len(t):
    if t[right] in s:
        if t[right] == s[left]:
            total += 1
            left += 1
            right += 1
        else:
            left += 1
    else:
        count += len(t) - total
        break
return count
"""
