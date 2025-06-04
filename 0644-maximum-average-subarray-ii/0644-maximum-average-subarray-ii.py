class Solution:
    def findMaxAverage(self, nums, k):
        max_val = max(nums)
        min_val = min(nums)
        prev_mid = max_val
        error = float('inf')

        while error > 1e-5:
            mid = (max_val + min_val) / 2
            if self.check(nums, mid, k):
                min_val = mid
            else:
                max_val = mid
            error = abs(prev_mid - mid)
            prev_mid = mid

        return min_val

    def check(self, nums, mid, k):
        sum_ = 0
        prev = 0
        min_sum = 0

        for i in range(k):
            sum_ += nums[i] - mid
        if sum_ >= 0:
            return True

        for i in range(k, len(nums)):
            sum_ += nums[i] - mid
            prev += nums[i - k] - mid
            min_sum = min(min_sum, prev)
            if sum_ >= min_sum:
                return True

        return False
