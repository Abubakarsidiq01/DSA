class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)
        
        return build(s) == build(t)

sol = Solution()
s = "ab#c"
t = "ad#c"
print(sol.backspaceCompare(s, t))

s = "ab##"
t = "c#d#"
print(sol.backspaceCompare(s, t))

s = "a#c"
t = "b"
print(sol.backspaceCompare(s, t))

