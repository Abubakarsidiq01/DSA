from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        # Condition 1: same set of characters
        for letter in word1:
            if letter not in word2:
                return False
        # Condition 1: same set of characters
        for x in word1:
            dic1[x] += 1
        for y in word2:
            dic2[y] += 1

        return sorted(dic1.values()) == sorted(dic2.values())
        
"""
if set(word1) != set(word2):
            return False
        
        # Condition 2: same frequency distribution
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        return sorted(count1.values()) == sorted(count2.values())
"""     
sol = Solution()
print(sol.closeStrings("abc", "bca"))
print(sol.closeStrings("a", "aa"))
print(sol.closeStrings("cabbba", "abbccc"))
print(sol.closeStrings("cabbba", "aabbss"))