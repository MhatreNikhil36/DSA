class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def find(s,e,t):
            if s<0 or e>=n:
                return -1
            m=None
            while s<=e:    
                
                m=(s + e) // 2
                print(s,m,e)
              
                if nums[m]==t:
                    return m
                elif nums[m]>t:
                    e=m-1
                elif  nums[m]<t:
                    s=m+1
                else:
                    return -1
            return -1
        Low=None
        High=None
        x=find(0,n-1,target)
        Low=x
        High=x
        c=Low
        while c>=0:
            print('low cal',c,Low)
            c=find(0,Low-1,target)
            if c>=0:
                Low=c
        c=High
    
        while c>=0:
            print('High cal',c,High)
            c=find(High+1,n-1,target)
            if c>=0:
                High=c

        return [Low,High]

    