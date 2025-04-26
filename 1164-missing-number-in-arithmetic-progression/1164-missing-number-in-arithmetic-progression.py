class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n=len(arr)
        s=arr[0]
        e=arr[-1]
        d=(e-s)//(n)
        for i in range(n):
            if arr[i]!=s+(i*d):
                return s+(i*d)
        return arr[i]
