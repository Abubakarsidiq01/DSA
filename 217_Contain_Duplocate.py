class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

        """
        ans = set()
        for num in nums:
            if num not in ans:
                ans.add(num)
            else:
                return True
        return False
        """
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    
    print(containsDuplicate(nums1))
    print(containsDuplicate(nums2))
    