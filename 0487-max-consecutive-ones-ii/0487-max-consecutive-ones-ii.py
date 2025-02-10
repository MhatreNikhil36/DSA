class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        zindex=None
        ans=0
        for r in range(len(nums)):
            if nums[r]==0:
                if zindex==None:
                    zindex=r
                else:
                    l=zindex+1
                    zindex=r
            ans=max(ans,r-l+1)
        return ans 


