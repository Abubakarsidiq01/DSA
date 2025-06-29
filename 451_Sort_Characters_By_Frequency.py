from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        return ''.join(alp * freq for alp, freq in sorted(dic.items(), key=lambda x: -x[1]))

solution = Solution()
print(solution.frequencySort("tree"))
print(solution.frequencySort("cccaaa"))
print(solution.frequencySort("Aabb"))
"""
dic = defaultdict(int)
for letter in s:
    dic[letter] += 1
lst = []
for key, value in dic.items():
    lst.append((key, value))
lst.sort(key=lambda x:x[1], reverse = True)
result = "".join(letter * freq for letter, freq in lst)
return result
"""