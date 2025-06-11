class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.data=[]
        self.data.append(deque(v1))
        self.data.append(deque(v2))
        self.switch=0

    def next(self) -> int:
        
        if self.data[self.switch]:
            x=self.data[self.switch].popleft()
            self.switch=(self.switch+1)%2
            return x
        else:
            self.switch=(self.switch+1)%2
            x=self.data[self.switch].popleft()
            return x

    def hasNext(self) -> bool:
        if self.data[self.switch] or self.data[(self.switch+1)%2]:
            return  True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())