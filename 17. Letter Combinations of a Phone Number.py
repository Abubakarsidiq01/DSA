class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        dic = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}
        result = []
        def backtrack(curr, i):
            if i == len(digits):
                result.append(curr)
                return
            for letter in dic[int(digits[i])]:
                backtrack(curr + letter, i + 1)

        backtrack("", 0)
        return result

sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("2"))