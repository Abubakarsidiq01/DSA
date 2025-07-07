from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        dic = defaultdict(int)
        for right in range (len(s)):
            dic[s[right]] += 1  # add to the dictionary
            while dic[s[right]] > 1: # if at a point the frquency is more than one
                dic[s[left]] -= 1 # start subtracting from the left till it reaches ! back
                left += 1
            ans = max(ans, right - left + 1)
        return ans
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring(""))
print(sol.lengthOfLongestSubstring(" "))
print(sol.lengthOfLongestSubstring("au"))
print(sol.lengthOfLongestSubstring("dvdf"))
print(sol.lengthOfLongestSubstring("anviaj"))