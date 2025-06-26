class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans=''
        s=s[::-1]
        c=0
        for i in range(len(s)):
            print(i,s[i],ans,k-c)
            if s[i]=='0':
                ans+='0'
            else:
                print('\t',2**i)
                if k-(c+2**i)>=0:
                    ans+='1'
                    c+=2**i

        return len(ans)