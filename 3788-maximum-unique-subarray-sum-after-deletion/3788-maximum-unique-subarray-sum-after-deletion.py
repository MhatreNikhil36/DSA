from collections import Counter
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen=set()
        ans=nums[0]
        seen.add(nums[0])
        for x in nums:
            if x not in seen :
                ans=max(ans+x,x,ans)
                seen.add(x)
        return ans 
