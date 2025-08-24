# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Mock implementation for testing
picked_number = 6  # This would be set by the system in LeetCode

def guess(num: int) -> int:
    if num > picked_number:
        return -1
    elif num < picked_number:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left , right = 1 , n
        while left <= right:
            mid = (left + right)//2
            ans = guess(mid)

            if ans == 0:
                return mid
            elif ans == -1:
                right = mid -1
            else:
                left = mid + 1

# Test cases
solution = Solution()

# Test 1: n=10, picked=6
picked_number = 6
result1 = solution.guessNumber(10)
print(f"Test 1: n=10, picked={picked_number}, result={result1}")

# Test 2: n=1, picked=1
picked_number = 1
result2 = solution.guessNumber(1)
print(f"Test 2: n=1, picked={picked_number}, result={result2}")

# Test 3: n=2, picked=1
picked_number = 1
result3 = solution.guessNumber(2)
print(f"Test 3: n=2, picked={picked_number}, result={result3}")