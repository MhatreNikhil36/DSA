class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        l=0
        c=0
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i+1]:
                if nums[i]>nums[l] and nums[i]>nums[i+1]:
                    c+=1
                elif nums[i]<nums[l] and nums[i]<nums[i+1]:
                    c+=1
                l=i
            
        return c

                
