class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        from typing import List

        max_or = 0
        for x in nums:
            max_or |= x  # Bitwise OR
        
        ans = 0
        
        def backtrack(i, curr_or):
            nonlocal ans
            if i == len(nums):
                if curr_or == max_or:
                    ans += 1
                return
            # Include nums[i]
            backtrack(i + 1, curr_or | nums[i])
            # Exclude nums[i]
            backtrack(i + 1, curr_or)
        
        backtrack(0, 0)
        return ans
