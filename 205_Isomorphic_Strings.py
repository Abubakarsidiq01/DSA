class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {} # dic of s to t
        dic2 = {} # dic of t to s
        for i in range (len(s)):
            if (s[i] in dic1 and dic1[s[i]] != t[i]) or (t[i] in dic2 and dic2[t[i]] != s[i]):
                return False
            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]
        return True

sol = Solution()
print(sol.isIsomorphic("egg", "add"))
print(sol.isIsomorphic("foo", "bar"))
print(sol.isIsomorphic("paper", "title"))
print(sol.isIsomorphic("ab", "aa"))