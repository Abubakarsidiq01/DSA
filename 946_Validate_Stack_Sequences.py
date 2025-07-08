class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not popped
sol = Solution()
print(sol.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(sol.validateStackSequences([1,2,3,4,5], [4,3,5,2,1]))
print(sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))