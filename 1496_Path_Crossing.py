class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x = y = 0       #Starting Point
        visited.add((x, y))

        for direction in path:  #Tracking Movement:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            if (x, y) in visited: #Check for Repeats
                return True
            visited.add((x, y))  #Store Visited Coordinates

        return False

"""
To determine if the path crosses itself, you need to track the coordinates you visit on the 2D plane  not just the directions.
"""
path = "NES"
sol = Solution()
print(sol.isPathCrossing(path))