from collections import  OrderedDict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        req=set(list(target))
        available=set(list(source))
        for x in req:
            if x not in available:
                return -1
        it=1
        n=len(source)
        m=len(target)
        i=0
        j=0
        while j<m:
            if i>=n:
                i=i%n
                it+=1
            if target[j]==source[i]:
                j+=1
                i+=1
            else:
                while target[j]!=source[i]:
                    i+=1
                    if i>=n:
                        i=i%n
                        it+=1
                j+=1
                i+=1
        return it


        
        