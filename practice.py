def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x - 1]
        ans.append(curr < limit)

    return ans

print(answer_queries([1, 6, 3, 2, 7, 2], [[0, 3], [3, 5], [2, 4]], 13))

lst = [3, 6, 2, 8, 1, 4, 1, 5]
ans = [lst[0]]
for i in range(1, len(lst)):
    ans.append(lst[i] + ans[-1])

for i in range(3,7):
    print(ans[i])

print(lst[:3])
print(lst[1:])



