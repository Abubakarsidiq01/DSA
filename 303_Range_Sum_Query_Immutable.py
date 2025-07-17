class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefixsum = [nums[0]]
        for i in range (1, len(nums)):
            self.prefixsum.append(self.prefixsum[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
      return self.prefixsum[right] - self.prefixsum[left]  + self.nums[left]
        
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)