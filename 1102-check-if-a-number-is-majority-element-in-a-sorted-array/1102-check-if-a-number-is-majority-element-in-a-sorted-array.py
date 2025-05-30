class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        c=Counter(nums)
        l=len(nums)
        ansC=0
        ans=None
        for x in c:
            if c[x]>ansC:
                ansC=c[x]
                ans=x
        # print(ans,ansC)
        if ansC>(l//2 ) and ans==target:
            return True
        return False