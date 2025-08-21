import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        
        while left <= right:
            mid = (left + right)//2 # a k candidate (k in the question, mid in the binary search)
            # calculate hours at speed mid
            hours = sum(math.ceil(p/mid) for p in piles)
            if hours <= h:
                ans = mid
                right = mid -1  # possible answer
            else:
                left = mid + 1  # need faster speed
        return ans #minimum k
solution = Solution()
print(solution.minEatingSpeed([3,6,7,11], 8))
solution.minEatingSpeed([3,6,7,11], 8)
print(solution.minEatingSpeed([30,11,23,4,20], 5))
solution.minEatingSpeed([30,11,23,4,20], 5)
print(solution.minEatingSpeed([30,11,23,4,20], 6))
solution.minEatingSpeed([30,11,23,4,20], 6)