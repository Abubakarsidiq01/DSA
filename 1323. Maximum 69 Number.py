class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = list(str(num))
        for i in range (len(nums)):
            if nums[i] != "9":
                nums[i] = "9"
                break
        return int("".join(nums))
s = Solution()
print(s.maximum69Number(9669))
print(s.maximum69Number(9999))
print(s.maximum69Number(9996))
print(s.maximum69Number(9999))
print(s.maximum69Number(9999))