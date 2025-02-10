class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        charmap=dict()
        l=0
        
        ans=0
        for r in range(len(s)):
            charmap[s[r]]=r
            if len(charmap)>k:
                tbd=min(charmap.values())
                del charmap[s[tbd]]
                l=tbd+1
            ans=max(ans,r-l+1)
        return ans 