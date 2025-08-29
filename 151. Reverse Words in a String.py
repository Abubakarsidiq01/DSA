class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.split()
        print(new_s)
        left = 0
        right = len(new_s) - 1

        while left < right:
            new_s[left], new_s[right] = new_s[right], new_s[left]
            left += 1
            right -= 1
        return " ".join(new_s)
solution = Solution()
print(solution.reverseWords("the sky is blue"))
solution.reverseWords("the sky is blue")
print(solution.reverseWords("  hello world  "))
solution.reverseWords("  hello world  ")
print(solution.reverseWords("a good   example"))
solution.reverseWords("a good   example")