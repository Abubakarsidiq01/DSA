class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "".join([c for c in s if c.isalnum()]).lower()
        return valid == valid[::-1]
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
print(sol.isPalindrome("0P"))
print(sol.isPalindrome("0P0"))
print(sol.isPalindrome("0P0"))