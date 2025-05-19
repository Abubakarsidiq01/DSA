from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = set(ransomNote)
        ans = []
        for letter in a:
            if ransomNote.count(letter) <= magazine.count(letter):
                ans.append(letter)
        
        return len(ans) == len(a)
    
sol = Solution()
ransomNote = "a"
magazine = "b"
print(sol.canConstruct(ransomNote, magazine))


"""
dic = defaultdict(int)
for letter in ransomNote:
    dic[letter] += 1

dic2 = defaultdict(int)
for alp in magazine:
    if alp in ransomNote:
        dic2[alp] += 1


ans = []
for key in dic:
    if dic[key] <= dic2[key]:
        ans.append(key)
return len(ans) == len(set(ransomNote))
"""