import random
class RandomizedSet:

    def __init__(self):
        self.mod=1000
        self.data=[None for i in range(self.mod)]
        

    def insert(self, val: int) -> bool:
        k=val%self.mod
        if self.data[k]==None:
            self.data[k]=val
            return True
        if  isinstance(self.data[k], list):
            if val in self.data[k]:
                return False
            else:
                self.data[k].append(val)
                return True
        if self.data[k]!=None:
            if self.data[k]==val:
                return False
            self.data[k]=[self.data[k],val]
            return True
    
        

    def remove(self, val: int) -> bool:
        k=val%self.mod
        if self.data[k]==None:
            return False
        if  isinstance(self.data[k], list):
            if val in self.data[k]:
                self.data[k].remove(val)
                return True
            else:
                return False
        if self.data[k]!=None:
            if self.data[k]==val:
                self.data[k]=None
                return True
            return False
  
        
    def getRandom(self) -> int:
        n=len(self.data)
        if n==0:
            return None
        flat_list = []
        
        # Flatten the list to handle nested lists
        def flatten_list(lst):
            for item in lst:
                if item!=None:
                    if  isinstance(item, list):
                        flatten_list(item)
                    else:
                        flat_list.append(item)
        
        flatten_list(self.data)
        # print(flat_list)
        if flat_list:
            return random.choice(flat_list)
        return None


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()