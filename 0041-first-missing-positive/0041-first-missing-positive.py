class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # heapify(nums)
        
        
        # p=heappop(nums)
        # while nums and p<0 :
        #     p=heappop(nums)
        # print(p)
        # start=min(nums)
        # if p:
        #     start=min(start,p)
        # if start>1:
        #     return 1
        # while nums:
        #     c=heappop(nums)
        #     if c-p>1:
                
        #         return p+1
        #     p=c
        # if p+1<1:
        #     return 1
        # return p+1
        heapify(nums)  # Ensure nums is a heap

        if not nums:  # Handle empty input
            return 1

        p = heappop(nums)  # Get the smallest element
        while nums and p < 0:
            p = heappop(nums)  # Keep popping until we find a non-negative number

        # If nums was all negative or empty
        if p < 0:
            return 1

        start = float('inf')  # Initialize start with a large number
        if nums:
            start = min(nums)  # Get the minimum of the remaining numbers

        # Update start based on p
        if p < start:
            start = p

        if start > 1:  # If the smallest is greater than 1
            return 1

        while nums:
            c = heappop(nums)
            if c - p > 1:  # Check the gap between current and previous
                return p + 1
            p = c

        return p + 1    