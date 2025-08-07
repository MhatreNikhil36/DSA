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
                res.extend(res) 
                
            elif x=='%':
                res.reverse()
            # print('\t',res)
        return ''.join(res)
