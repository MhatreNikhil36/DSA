class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,[-nums[i],i])
        
        ans=[]
        for i in range(k):
            x=heapq.heappop(heap)
            heapq.heappush(ans,[x[1],x[0]])
        print(ans)
        res=[]
        while ans:

            res.append(-heapq.heappop(ans)[1])
        return res