from collections import Counter
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        start=heapq.heappop(nums)
        subCount=1
        while nums:
            c=heapq.heappop(nums)
            if c-start>k:
                subCount+=1
                start=c
        return subCount