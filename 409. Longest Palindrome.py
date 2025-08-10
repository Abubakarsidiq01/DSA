from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        count = 0
        odd_found = False
        for key in dic.values():
            if key % 2 == 0:
                count += key
            else:
                count += key - 1 #Use count - 1 for odd counts (so they become even and usable in pairs)
                odd_found = True
        if odd_found: #Keep track if any odd count exists; if yes, add +1 at the end for the cente
            count += 1
        return count
sol = Solution()
print(sol.longestPalindrome("abccccdd"))