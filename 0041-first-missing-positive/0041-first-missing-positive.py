class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0

        while i<n:
            ci= nums[i] -1
            if   0 <= ci < n and nums[i] > 0 and nums[i] != nums[ci]:
                 nums[i], nums[ci] = nums[ci], nums[i]
            else:
                i+=1
        # print(i)
        # print(nums)
        c=1
        for i in range(n):
            # print(i,c)
            if nums[i]!=i+1:
                return i+1
        return  n+1