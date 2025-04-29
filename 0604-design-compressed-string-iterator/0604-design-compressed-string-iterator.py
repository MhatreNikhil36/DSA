class StringIterator:

    def __init__(self, compressedString: str):
        self.comp=deque(list(compressedString))
        self.currs=None
        self.currc=0
        

    def next(self) -> str:
        if not self.comp and self.currc==0:
            return " "
        if self.currc==0:
            self.currs=self.comp.popleft()
            p=0
            while self.comp and self.isdigit(self.comp[0]):
                x=self.comp.popleft()
                self.currc=(self.currc*(10**p))+int(x)
                p+=1
        # print(self.currc)
        self.currc-=1
        return self.currs
    
    def isdigit(self,x):
        if x in {'0','1','2','3','4','5','6','7','8','9'}:
            return True
        return False
        

    def hasNext(self) -> bool:
        if self.comp or self.currc>0:
            return True
        return False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()