class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i=0
        while i<len(nums) and nums[i]<=0:
            i+=1
        i-=1
        print(i,len(nums)-i-1)
        ans=len(nums)-i-1
        if ans>i+1:
            return ans 
        while i>=0 and  nums[i]==0:
            print(i)
            i-=1
        return max(ans,i+1) 

        