class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        condensed=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                condensed.append(nums[i])
        c=0
        nums=condensed
        n=len(condensed)
        for i in range(n):
            l=i-1
            r=i+1
            if l>=0 and r<n:
                # print(nums[l],nums[i],nums[r])
                if nums[i]>nums[l] and nums[i]>nums[r]:
                    c+=1
                    # print(nums[i])
                if nums[i]<nums[l] and nums[i]<nums[r]:
                    c+=1
                    # print(nums[i])
        return c

                
