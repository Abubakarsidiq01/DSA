import math
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        left, right = 1, 10 ** 7
        ans = -1
         
        while left <= right:
            mid = (left + right)//2 # candidate speed (k)

            total_time = 0
        
            # all but last train: must round up
            for d in dist[:-1]:
                total_time += math.ceil(d / mid)
        
            # last train: no rounding
            total_time += dist[-1] / mid

            if total_time <= hour:
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans
solution = Solution()
print(solution.minSpeedOnTime([1,3,2], 2.7))
solution.minSpeedOnTime([1,3,2], 2.7)
print(solution.minSpeedOnTime([1,3,2], 1.9))
solution.minSpeedOnTime([1,3,2], 1.9)
print(solution.minSpeedOnTime([1,3,2], 6))
solution.minSpeedOnTime([1,3,2], 6)
"""
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1
        left, right = 1, 10 ** 7
       
        while left <= right:
            mid = (left + right)//2 # candidate speed (k)

            total_time = 0
        
            # all but last train: must round up
            for d in dist[:-1]:
                total_time += math.ceil(d / mid)
        
            # last train: no rounding
            total_time += dist[-1] / mid

            if total_time <= hour:
                
                right = mid -1
            else:
                left = mid + 1
        return left
"""