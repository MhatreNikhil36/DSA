class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs)==1:
            return min(costs[0])
        ans=[[0,0,0] for i  in range(len(costs))]
        print(ans)
        ans[0]=costs[0]
        op=((1,2),(0,2),(0,1))
        for i in range(1,len(costs)):
            for x in range(3):
                o=math.inf
                print(ans[i-1])
                if x==0:
                    o=min(ans[i-1][1],ans[i-1][2])
                elif x==1:
                    o=min(ans[i-1][0],ans[i-1][2])
                else:
                    o=min(ans[i-1][0],ans[i-1][1])
                print(x,o)
                ans[i][x]=costs[i][x]+o
        return min(ans[-1])
                