class Solution:
    def removeDuplicates(self, s: str) -> str:
        a = list(s)
        b = []
        while a:
            if b and a[-1] == b[-1]:  
                a.pop()
                b.pop()
            else:
                c = a.pop()
                b.append(c) 
    
        return "".join(reversed(b))      
    
sol = Solution()
s = "abbaca"
print(sol.removeDuplicates(s))

s = "azxxzy"
print(sol.removeDuplicates(s))

