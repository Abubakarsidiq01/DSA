class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int: 
        total = 0
        boxTypes.sort(key=lambda x : x[1], reverse = True )
        print(boxTypes)
        for i in range(len(boxTypes)):      
            if truckSize and truckSize >= boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                total += (boxTypes[i][1] * boxTypes[i][0])
            else:
                if truckSize and truckSize <= boxTypes[i][0]:
                    total += (boxTypes[i][1] * truckSize)
                    truckSize -= truckSize
            print(total ,"=", truckSize)
        return total
s = Solution()
print(s.maximumUnits([[1,3],[2,2],[3,1]], 4))
print(s.maximumUnits([[1,3],[2,2],[3,1]], 4))
