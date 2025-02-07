
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        main=dict()
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                k=nums[i]*nums[j]
                if k not in main:
                    main[k]=set()
                
                main[k].add((nums[i],nums[j]))
                j+=1
        # for x in main:
        #     print(x,main[x])      
        ans=0
        for x in main:
            f=len(main[x])
            ans+=((f-1)*f/2)*8


        return int(ans)
