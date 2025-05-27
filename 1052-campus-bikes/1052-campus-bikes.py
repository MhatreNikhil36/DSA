class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dis=[]
        for n in range(len(workers)):
            for m in range(len(bikes)):
                x,y=workers[n]
                i,j=bikes[m]    
                d=abs(i-x)+abs(j-y)
                heapq.heappush(dis,(d,n,m))
                # print(d,n,m)
        taken=set()
        ans=[None for i in range(len(workers))]
        for i in range(len(workers)):
            # print(ans)
            # print(taken)
            # print(dis,'\n'*4)
            d,w,b=heapq.heappop(dis)
            while ans[w]!=None or b in taken:
                d,w,b=heapq.heappop(dis)
            taken.add(b)
            ans[w]=b
        return ans 
                