class Solution:
    def kthCharacter(self, k: int) -> str:
        print(ord('a'))
        print(ord('z'))
        # i got that a ot  z is 97 to 99
        # print(ord(99))
        s=[97,98,98,99]
        while  k>len(s):
            n=len(s)
            for i in range(n):
                c=s[i]+1
                if c>122:
                    c=97
                s.append(c)
        print(k)
        # print(s[k])
        print(s)     
      
        return chr(s[k-1])
        
        
