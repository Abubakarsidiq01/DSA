class Solution:
    def destCity(self, paths:list[list[str]]) -> str:
        fromcity = set()

        for row in paths:
            fromcity.add(row[0])
        for col in paths:
            if col[1] not in fromcity:
                return col[1]
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
sol = Solution()
print(sol.destCity(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(sol.destCity(paths))

paths = [["A","B"]]
print(sol.destCity(paths))


