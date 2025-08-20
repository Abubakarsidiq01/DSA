import bisect
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        nums.sort()
        lst = list(accumulate(nums))
        return [bisect.bisect_right(lst, num) for num in queries]
        """
        nums.sort()
        total = 0
        num = [(total := total + n) for n in nums]

        ans = []
        for q in queries:
            i = bisect.bisect_right(num, q)
            ans.append(i)
        return ans
       


        """
        nums.sort()
        queries.sort()
        count = total = 0
        lst = []
        if nums[0] > queries[0]:
            lst.append(0)
            return lst
      
        for num in queries:
            j = 0
            while total < num:
                total += nums[j]
                j += 1
                count += 1
            lst.append(count)
            count = 0

        return lst
        """   
solution = Solution()
print(solution.answerQueries([4,5,2,1], [3,10,21]))
solution.answerQueries([4,5,2,1], [3,10,21])
print(solution.answerQueries([2,3,4,5], [1]))
solution.answerQueries([2,3,4,5], [1])
print(solution.answerQueries([1,2,3,4,5], [3]))
solution.answerQueries([1,2,3,4,5], [3])
print(solution.answerQueries([1,2,3,4,5], [10]))
solution.answerQueries([1,2,3,4,5], [10])