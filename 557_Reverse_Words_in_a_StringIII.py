class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])

solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
