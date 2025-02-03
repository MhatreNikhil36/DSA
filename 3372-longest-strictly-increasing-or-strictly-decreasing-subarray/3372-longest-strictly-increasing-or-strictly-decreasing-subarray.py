class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        inc=[1]*n
        dec=[1]*n
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                dec[i]=dec[i-1]+1
            elif nums[i-1]<nums[i]:
                inc[i]=inc[i-1]+1
        return max(max(inc),max(dec))
