class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        count = 0
        ans = count
        for num in gain:
            count = count - (-num) # basically the same with count += num 
            ans = max(ans, count)
        return max(count, ans)
sol = Solution()
gain = [-5,1,5,0,-7]
print(sol.largestAltitude(gain))

gain = [-4,-3,-2,-1,4,3,2]
print(sol.largestAltitude(gain))


