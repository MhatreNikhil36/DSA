class Solution:
    def clearDigits(self, s: str) -> str:
        ans=[]
        for x in s:
            if x.isdigit():
                if ans:
                    ans.pop()
            else:
                ans.append(x)
        return ''.join(ans)