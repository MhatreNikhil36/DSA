class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowHeap=[]
        n=len(nums)
        for i in  range(k):
            heapq.heappush(windowHeap,-nums[i])
        ans=[]
        ans.append(-windowHeap[0])
        outgoing=[]
        for  i in range(k,n):
            # print(windowHeap,'\n out,',outgoing)
           
            heapq.heappush(outgoing,-nums[i-k])
            heapq.heappush(windowHeap,-nums[i])
            
            while outgoing  and windowHeap and  outgoing[0]==windowHeap[0]:
                heapq.heappop(outgoing)
                heapq.heappop(windowHeap)
            ans.append(-windowHeap[0])
        return  ans 

