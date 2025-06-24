class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        ans = count = 0

        for char in s[:k]:
            if char in vowel:
                count += 1
        ans = count

        for i in range(k, len(s)):
            if s[i] in vowel:
                count += 1
            if s[i-k] in vowel:
                count -= 1
            ans = max(ans, count)
        return ans

solution = Solution()
print(solution.maxVowels("abciiidef", 3))

"""
first check the how man vowels are in the first valid subarray and then let that be your answer.
Iterate from the next letter and then remove the first letter that will make it invalid subarray
and keep updating your answer
"""