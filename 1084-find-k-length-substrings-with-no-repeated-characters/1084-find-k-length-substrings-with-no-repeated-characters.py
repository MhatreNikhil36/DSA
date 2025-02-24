from collections import deque 
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        char=set()
        window=deque()
        ans=0
        for i in range(len(s)):
            if not char and window:
                char.add(s[i])
                widow.append([i,s[i]])
            if s[i] in char:
                p,v=window.popleft()
                while window and v!=s[i]:
                    char.remove(v)
                    p,v=window.popleft()
            char.add(s[i])
            window.append([i,s[i]])

                
            # if window and window[-1][0]-window[0][0]>=k-1:
            if len(char)>=k:
                p,v=window.popleft()
                char.remove(v)
                ans+=1
        return ans

