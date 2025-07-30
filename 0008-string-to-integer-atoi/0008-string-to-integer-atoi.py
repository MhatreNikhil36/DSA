class Solution:
    def myAtoi(self, s: str) -> int:
        digits={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        signs={'-':-1,'+':1}
        integer=None
        sign=None
        for x in s:
            if x in digits:
                if  not  sign:
                    sign=1
                if not  integer:
                    integer=digits[x]
                    
                else:
                    if integer==0:
                        integer=digits[x]
                    else:
                        integer=(integer*10)+digits[x]
            elif  x in signs:
                if  sign:
                    break
                else:
                    sign=signs[x]
            elif  sign!=None or integer!=None :
                break
            elif x==' ':
                continue
            else:
                break
        if  not integer:
            return 0
        if not  sign:
            sign=1
        if integer>=2**31:
            if sign<0:
                integer=2**31 
            else:
                integer=2**31 -1
        # print(sign,integer)
        return sign*integer
                