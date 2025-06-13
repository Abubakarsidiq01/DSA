from collections import deque

class StockSpanner:

    def __init__(self):
        self.q = deque()

    def next(self, price: int) -> int:
        count = 1
        while self.q and self.q[-1][0] <= price:
            prev_price, prev_span = self.q.pop()
            count += prev_span
        self.q.append((price, count))
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
