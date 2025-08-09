class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        count = total = 0
        costs.sort()
        for num in costs:
            if (total + num) <= coins:
                total += num
                count += 1
            else:
                break
        return count
sol = Solution()
print(sol.maxIceCream([1,3,2,4,1], 7))
print(sol.maxIceCream([10,6,8,7,7,8], 5))
print(sol.maxIceCream([1,6,3,1,2,5], 20))
print(sol.maxIceCream([1,6,3,1,2,5], 10))
print(sol.maxIceCream([1,6,3,1,2,5], 15))
print(sol.maxIceCream([1,6,3,1,2,5], 25))
print(sol.maxIceCream([1,6,3,1,2,5], 30))
print(sol.maxIceCream([1,6,3,1,2,5], 35))