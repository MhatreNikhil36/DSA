class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<=j:
            t=s[j]
            s[j]=s[i]
            s[i]=t
            i+=1
            j-=1
        print(s)
        i=0
        j=0
        while i<len(s):
            while j<len(s) and s[j]!=' ':
                j+=1
            new=j+1
            j-=1
            while i<len(s) and  j<len(s) and i<j:
                t=s[i]
                s[i]=s[j]
                s[j]=t
                i+=1
                j-=1
            i=new
            j=new
        print(s)
        