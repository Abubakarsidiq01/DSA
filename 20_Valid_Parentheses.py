class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "{": "}","[": "]"}  # store all the opening as the key and the closing as the value since there will be an opening before they can be a closing.

        for bracket in s:
            if bracket in dic: 
                stack.append(bracket) # if it is an opening bracket, stack it
            else:
                if not stack: # else it will be a closing bracket so is the stack empty, 
                    return False
                open_bracket = stack.pop() #else pop the last bracket that was stack that need closing.
                if dic[open_bracket] != bracket: #check if this bracket that need closing the same thing as the current bracket.
                    return False
        return not stack      

sol = Solution()
s = "([)]"
print(sol.isValid(s))

s = "()"
print(sol.isValid(s))

s = "()[]{}"
print(sol.isValid(s))


