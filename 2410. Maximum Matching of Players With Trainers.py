class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        while players and trainers:
            if players[-1] <= trainers[-1]:
                count += 1
                players.pop()
                trainers.pop()
            else:
                players.pop()
        return count
sol = Solution()
print(sol.matchPlayersAndTrainers([4,7,9,5], [6,2,3,8]))