class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # size of the subseq can range  from 1 to n
        # first  find all single digit eligible candidates
        # make sure the elements are arranges in an asending  order 
        # now if sum of first and last element is <=target then every subset between i and j is an eligible subset
        # now if i know i and j candidates to form a subsequece then how many subsequeence do we get (j-i)!
        nums.sort()
        ans=0
        n=len(nums)-1
        mod = 10 ** 9 + 7
        # for i in nums:
        #     if i*2<=target:
        #         ans+=1
        
        s=0
        e=n
        print('start',ans)
        while s<=e:
            if nums[s]+nums[e]<=target:
                ans+=pow(2, e - s, mod)
                s+=1
            else:
                e-=1
             
        return ans%mod