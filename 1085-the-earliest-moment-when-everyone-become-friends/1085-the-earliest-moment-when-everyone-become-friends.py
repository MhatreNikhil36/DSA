class uf:
    
    def __init__(self,n):
        self.parent=dict()
        self.rank=dict()
        self.count = n 
        for i in range(n):
            self.parent[i]=i
            self.rank[i]=1
    
    def find(self,x):
        while self.parent[x]!=x:
            x=self.parent[x]
        return self.parent[x]
    
    def union(self,x,y):
        a=self.find(x)
        b=self.find(y)
        if a==b:
            # print('already linked',self.parent)
            return False
        if self.rank[a]>self.rank[b]:
            self.parent[b]=a
            self.rank[a]+=1
 
        else:
            self.parent[a]=b
            self.rank[b]+=1
        self.count-=1
        # print(self.parent)
        if self.count==1:
            return True
        return False
import heapq
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friends=uf(n)

        heapq.heapify(logs)
        while logs:

            time,x,y=heapq.heappop(logs)
            # print(time,x,y)
            known=friends.union(x,y)
            if known:
                return time 

        return -1


