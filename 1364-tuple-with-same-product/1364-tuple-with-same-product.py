
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        main=dict()
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                k=nums[i]*nums[j]
                if k not in main:
                    main[k]=0
                main[k]+=1  
                j+=1   
        ans=0
        for x in main:
            f=main[x]
            ans+=((f-1)*f/2)*8


        return int(ans)
