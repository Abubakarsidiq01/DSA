from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        dic = {}
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack.pop()] = num # for every number, use the next higher number as the value of the key
            stack.append(num)
        return [dic.get(i, -1) for i in nums1] #getting the key and returning the value in a list. if no value return the -1 as the defualt value.

sol = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(sol.nextGreaterElement(nums1, nums2))





"""
q1 = deque(nums1)
q2 = deque()
demo = []
ans = []

while q1:
    for i in range(len(nums2)):
        if nums2[i] == q1[0]:
            q2.append(nums2[i])
            print("1", q1)
            print(q2)
            for j in range(i + 1, len(nums2)):
                if nums2[j] > q2[0]:
                    demo.append(nums2[j])
            try:
                ans.append(demo[0])
            except IndexError:
                ans.append(-1)
    
    q1.popleft()
    q2.popleft()
    demo.clear()
return ans
"""

    

