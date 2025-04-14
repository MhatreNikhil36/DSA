class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rems = {0:-1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            rem = total % k
            if rem in rems:
                if i - rems[rem] >= 2:
                    return True
            else:
                rems[rem] = i
        return False

