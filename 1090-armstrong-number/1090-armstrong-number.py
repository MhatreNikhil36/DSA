class Solution:
    def isArmstrong(self, n: int) -> bool:
        rem=n*1
        p=0
        while n>0:
            n=n//10
            p+=1
        n=rem
        while n>0 :
            c=n%10
            n=n//10
            rem-=(c**p)
        if rem==0:
            return True 
        return  False 
