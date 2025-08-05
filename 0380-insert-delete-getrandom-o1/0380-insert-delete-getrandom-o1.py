class RandomizedSet:

    def __init__(self):
        self.data=[]
        self.keys=dict()

    def insert(self, val: int) -> bool:
        if val in self.keys:
            return False
        n=len(self.data)
        self.data.append(val)
        self.keys[val]=n
        return True

    def remove(self, val: int) -> bool:
        if val not in self.keys:
            return False
        
        delidx=self.keys[val]
        if delidx==len(self.data)-1:
            self.data.pop()
            del self.keys[val]
            return True
        self.data[delidx]=self.data[-1]
        self.keys[self.data[-1]]=delidx
        self.data.pop()
        del self.keys[val]
        return True

        

    def getRandom(self) -> int:
        return   random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()