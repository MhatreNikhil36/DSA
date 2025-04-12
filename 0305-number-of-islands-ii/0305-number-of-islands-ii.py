class uf:
    def __init__(self,n,m):
        self.parent={}
        self.rank={}
        self.gc=0
        for i in range(m):
            for j in range(n):
                self.rank[(i,j)]=1
                self.parent[(i,j)]=(i,j)

    def find(self,x):
 
        while self.parent[x]!=x:
            x=self.parent[x]
        return x

    def union(self,x,y):
        a=self.find(x)
        b=self.find(y)
        # print(self.gc,a,b,self.rank)
        if a!=b:

            if self.rank[a]>self.rank[b]:
                self.parent[b]=a
                self.rank[a]+=1
            else:
                self.parent[a]=b
                self.rank[b]+=1
    
    def addgrp(self):
        # print(self.gc)
        self.gc+=1
        return self.gc
    
    def getgrp(self):
        # print(self.gc)
        return self.gc
    
    def decgrp(self,c):
        # print(self.gc)
        self.gc-=c

    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        graph=uf(n,m)
        dir=((1,0),(-1,0),(0,1),(0,-1))
        ans =[]
        seen=set()
        for x,y in  positions :
            if (x,y) in seen:
                ans.append(graph.getgrp())
                continue
            isNew=True
            uc=set()
            for dx,dy in dir:
                i,j=x+dx,y+dy
                # print(i,j,seen)
                if 0<=i<m and 0<=j<n:
                    if (i,j) in seen:
                        isNew=False
                        # print('union')
                        uc.add(graph.find((x,y)))
                        uc.add(graph.find((i,j)))
                        graph.union((x,y),(i,j))
        
            # print('u count',uc)
            if len(uc)>1:
                graph.decgrp(len(uc)-2)
            if isNew:
                gc=graph.addgrp()
            ans.append(graph.getgrp())
            seen.add((x,y))
        return ans 



                




