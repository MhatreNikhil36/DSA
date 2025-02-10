class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans=0
        i=0
        r=0
        map=dict()
        while r<len(s):
            
            map[s[r]]=r
            if len(map)>2:
                tbd=min(map.values())
                del map[s[tbd]]
                i=tbd+1
            ans=max(ans,r-i+1)
            r+=1
        return ans