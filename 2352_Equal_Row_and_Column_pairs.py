
from collections import defaultdict
class Solution:
    def equalPairs(grid: list[list[int]]) -> int:
        dic = defaultdict(int)  # The first dic is storing the row as key and the freq as value
        for row in grid:
            dic[tuple(row)] += 1 # You have to convert to a tuple because a list can't be a key.

        dic2 = defaultdict(int) #storing the column as a tuple and the frquency as value
        for col in range(len(grid[0])):
            store = []
            for row in range(len(grid)):
                store.append(grid[row][col])
            dic2[tuple(store)] += 1

        ans = 0
        for arr in dic:  # if it is in the row dic, it has to be in the column dic for it to be a pair
            ans += dic[arr] * dic2[arr]
        return ans
    
    grid = [[3,2,1],[1,7,6],[2,7,7]]   
    print(equalPairs(grid))        
 


        


        