from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size

    def next(self, val: int) -> float:
        
        self.q.append(val)
        size = self.size
        if len(self.q) > size:
            self.q.popleft()
            
        currentSum = sum(self.q)
        total = currentSum / size
        
        return total
    
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))  



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)