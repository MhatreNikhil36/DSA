class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        p=nums[0]%2
        for i in range(1,len(nums)):
            c=nums[i]%2
            if c==p:
                return False
            p=c
        return True 