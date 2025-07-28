class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc=0
        dec=0
        # 1 for increasing 0  for decreasing 

        for i  in  range(len(nums)-1):
    
            if nums[i]>nums[i+1] :
                dec+=1
            elif nums[i]<nums[i+1]:
                inc+=1
        if inc>0 and dec>0:
            return False
        return True


