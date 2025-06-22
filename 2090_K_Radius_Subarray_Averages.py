class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ans = [-1] * len(nums)
        if len(nums) <= 2*k:
            return ans

        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)

        a = 0
        b = (2*k) + 1
        c = k
         
        for i in range (k*2, len(result)):
            avg = (result[i] - result[a] + nums[a])//b
            ans[c] = avg
            a += 1
            c += 1
            print(avg)
        return ans       
solution = Solution()
print(solution.getAverages([7,4,3,9,1,8,5,2,6], 3))
