from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))

