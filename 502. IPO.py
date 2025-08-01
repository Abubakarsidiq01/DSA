import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Pair each project’s capital with its profit
        projects = list(zip(capital, profits))
        # Sort projects by capital required
        projects.sort()
        
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            # Add all projects that can be afforded to the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # use -profit for max-heap
                i += 1

            if not max_heap:
                break  # No affordable projects left

            # Choose the most profitable available project
            w += -heapq.heappop(max_heap)

        return w
s = Solution()
print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
print(s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
print(s.findMaximizedCapital(1, 0, [1, 2, 3], [0, 1, 2]))
print(s.findMaximizedCapital(1, 0, [1, 2, 3], [0, 1, 2]))