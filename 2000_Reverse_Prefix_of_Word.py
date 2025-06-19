class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
            
        a = word.find(ch)
        result = word[a::-1] + word[a+1:]
        return result

solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))
