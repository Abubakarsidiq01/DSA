class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        store = []
        for letter in s:
            if letter not in store:
                store.append(letter)
            else:
                count += 1
                store.clear()
                store.append(letter)
        return count
sol = Solution()
print(sol.partitionString("abacaba"))