class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost=0
        if len(sticks)==0:
            return 0

        while len(sticks)>1:
            x=heapq.heappop(sticks)
            y=heapq.heappop(sticks)
            cost+=x+y
            print(x,y,cost)
            heapq.heappush(sticks,x+y)
        return cost
