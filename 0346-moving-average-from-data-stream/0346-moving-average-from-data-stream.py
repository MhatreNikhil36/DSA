from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        print(size)
        self.size=size
        self.data=deque()
        self.sum=0

    def next(self, val: int) -> float:
        if not self.data:
            self.data.append(val)
            self.sum+=val
            return self.sum/1
        self.data.append(val)
        n=len(self.data)
        if n>self.size:
            leaving=self.data.popleft()
            self.sum-=leaving
            n-=1
        self.sum+=val
        # print(self.data,self.sum,n)
        return self.sum/n



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)