class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        count = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1
        return count
s = Solution()
print(s.numRescueBoats([1, 2], 3))
print(s.numRescueBoats([3, 5, 3, 4], 5))
print(s.numRescueBoats([3, 2, 2, 1], 3))
print(s.numRescueBoats([3, 5, 3, 4], 5))
print(s.numRescueBoats([3, 5, 3, 4], 5))