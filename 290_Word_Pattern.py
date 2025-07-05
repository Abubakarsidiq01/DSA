class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        dic1 = {}
        dic2 = {}
        print(s)
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if (pattern[i] in dic1 and dic1[pattern[i]] != s[i]) or (s[i] in dic2 and dic2[s[i]] != pattern[i]):
                return False
            dic1[pattern[i]] = s[i]
            dic2[s[i]] = pattern[i]
        return True
"""
 def wordPattern(self, pattern: str, s: str) -> bool:
        dict={}
        words=s.split()
        
        if(len(pattern)!=len(words)):
            return False

        for i in range(len(pattern)):
            if pattern[i] in dict.keys():
                if dict[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in dict.values(): # if the key is not in the dic but the value is used.
                    return False
                dict[pattern[i]]=words[i]
        return True
"""
sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))
print(sol.wordPattern("abba", "dog cat cat fish"))
print(sol.wordPattern("aaaa", "dog cat cat dog"))
print(sol.wordPattern("abba", "dog dog dog dog"))