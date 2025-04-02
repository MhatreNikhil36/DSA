class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        disheap=[]
        dismap={}
        for x,y in points:
            d=x*x +y*y
            if d not in dismap:
                dismap[d]=[]
                heapq.heappush(disheap,d)
            dismap[d].append((x,y))


        
        ans=[]
        while len(ans)<k:
            x=dismap[heapq.heappop(disheap)]
            if len(ans)+len(x)<k:
                ans+=x
            else:
                d=k-len(ans)
                ans+=x[:d]
                return ans 
        return ans 
        