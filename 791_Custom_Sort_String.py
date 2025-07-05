from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lst = []        # Stores letters from 'order' that are present in 's'
        n_lst = []      # Stores letters in 's' that are not in 'order'
        dic = defaultdict(int)  # Counts the frequency of each letter in 's' that is also in 'order'
        new_lst = []    # Stores the sorted letters, each repeated by its frequency in 's'

        # Loop 1: Collect only those characters from 'order' that actually exist in 's'
        for letter in order:
            if letter in s:
                lst.append(letter)

        # Loop 2: Go through 's' and:
        # - count how many times each letter (that's in 'order') appears (store in dic)
        # - collect letters not in 'order' (store in n_lst)
        for word in s:
            if word in lst:
                dic[word] += 1
            else:
                n_lst.append(word)

        # Loop 3: For each character from the filtered 'order' list (lst),
        # repeat it based on how many times it appeared in 's'
        for alp in lst:
            new_lst.append(alp * dic[alp])

        # Return the sorted letters first, followed by the leftover ones
        return "".join(new_lst) + "".join(n_lst)

sol = Solution()
print(sol.customSortString("cba", "abcd"))
print(sol.customSortString("cbafg", "abcd"))