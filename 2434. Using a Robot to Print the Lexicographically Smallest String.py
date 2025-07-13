class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)
        t = []     # robot's internal stack
        res = []   # final result (paper)
        min_char = 'a'

        for c in s:
            t.append(c)
            freq[c] -= 1

            # Update the minimum character still in s
            while freq[min_char] == 0 and min_char <= 'z':
                min_char = chr(ord(min_char) + 1)

            # Pop from t to result if top of t <= current min character left in s
            while t and t[-1] <= min_char:
                res.append(t.pop())

        return ''.join(res)
sol = Solution()
print(sol.robotWithString("bac"))
print(sol.robotWithString("cbacdcbc"))
print(sol.robotWithString("abacb"))
print(sol.robotWithString("aaabbbccc"))
print(sol.robotWithString("abc"))
print(sol.robotWithString("a"))
print(sol.robotWithString(""))
print(sol.robotWithString("z"))