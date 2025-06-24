class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = count = ans = 0
        for right in range(len(s)):
            count += abs(ord(s[right]) - ord(t[right]))
            if count <= maxCost:
                ans = max(ans, right - left + 1)
            else:
                count -= abs(ord(s[left]) - ord(t[left]))
                left += 1
        return ans
solution = Solution()
print(solution.equalSubstring("abcd", "bcdf", 3))

"""
#my first solution
lst = []
left = count = ans = 0
for i in range(len(s)):
    cost = abs(ord(s[i]) - ord(t[i]))
    lst.append(cost)
for right in range(len(lst)):
    count += lst[right]
    if count <= maxCost:
        ans = max(ans, right - left + 1)
    while count > maxCost:
        count -= lst[left]
        left += 1
return ans

# ord is used to determine the ASCII value
# Abs ensure there is no negeative cost
# Keep adding the cost of each index subtract to count as long as it is not more than the maxcost
# Then find the lenght of the window if it doesn't pass the maxCost and stir the max window
# If at any point the count pass the Maxcost, subtract the first index that is making it 
#  out of bound and upadte your ans
"""