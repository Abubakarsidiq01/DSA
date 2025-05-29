class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c.swapcase():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

        """
        # The first solution i came up with but then the if statement can be improved
        stack = []
        for c in s:
            if stack and stack[-1] == c.lower() and c == stack[-1].upper() or stack and stack[-1] == c.upper() and c == stack[-1].lower():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
        """
sol = Solution()
s = "abBA"
print(sol.makeGood(s))

s = "aA"
print(sol.makeGood(s))

