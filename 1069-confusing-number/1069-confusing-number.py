class Solution:
    def confusingNumber(self, n: int) -> bool:
        inverse={1:1,0:0,6:9 ,9:6,8:8}
        og=n
        res=0
        f=1
        stack=[]
        while n:
            c=n%10
            n=n//10
            if c not in inverse:
                return False
            else:
                stack.append(inverse[c])
        while stack:
            c=stack.pop()
            res+=f*c
            f*=10
        # print(og,res)
        return True if  res!=og else False
