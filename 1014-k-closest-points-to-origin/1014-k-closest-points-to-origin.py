class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for x in points:
            # print(x[0],x[1])
            dist=((x[0]*x[0])+(x[1]*x[1]))
            distances.append((dist,x))
        # print(distances)
        heapq.heapify(distances)
        # print(distances)
        
        ans=[]
        for x in range(k):
            p=heapq.heappop(distances)
            ans.append(p[1])
        # print(ans)
        return ans