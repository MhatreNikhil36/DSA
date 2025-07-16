class Solution:
    def countLetters(self, s: str) -> int:
        n=len(s)
        ans=0
        c=0
        m=dict()
        i=0
        while i<n:
            if i>0 and s[i]==s[i-1]:
                c+=1
            else:
                c=1
            ans+=c
            i+=1
        return ans


