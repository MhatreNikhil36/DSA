class Solution:
    def processStr(self, s: str) -> str:
        res=[]

        operations={'*','#','%'}
        for  x in s:
            # print(x)
            if  x not in operations:
                res.append(x)
            elif  x=='*':
                if res:
                    res.pop()
            elif x=='#':
                res=res+res
                
            elif x=='%':
                res=res[::-1]
            # print('\t',res)
        return ''.join(res)
