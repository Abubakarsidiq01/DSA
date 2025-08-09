from collections import Counter
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        n = len(arr)
        print(n)
        dic = Counter(arr)
        count = 0
        dicc = dict(sorted(dic.items(), key=lambda x:x[1], reverse = True))
        for key, value in dicc.items():
            n -= value
            count += 1
            if n <= len(arr)//2:
                
                break
        return count
sol = Solution()
print(sol.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(sol.minSetSize([7,7,7,7,7,7]))
print(sol.minSetSize([1,2,3,4,5,6,7,8,9,10]))
print(sol.minSetSize([1,1,1,1,1,1,1,1,1,1]))
print(sol.minSetSize([1,1,1,1,1,1,1,1,1,1]))

    