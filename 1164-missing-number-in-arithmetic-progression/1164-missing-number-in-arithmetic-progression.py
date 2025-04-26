class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n=len(arr)
        s=arr[0]
        e=arr[-1]
        d=(e-s)//(n)
        l=0
        r=n-1
        m=None
        while l<r:

            m=(l+r)//2
            if arr[m]==(s+m*d):
                l=m+1
            else:
                r=m
            
        return s+l*d
