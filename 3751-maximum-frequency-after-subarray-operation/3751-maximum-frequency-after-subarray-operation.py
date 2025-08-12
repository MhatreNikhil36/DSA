class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq,first,last = [0]*51,[-1]*51,[-1]*51
        res = 0

        # prefix sum occurences of k
        ps = [0]
        for a in nums: ps.append(ps[-1] + (1 if a ==k else 0)) #i + 1 is number of ks at or before index i

        # for each value you can target, find first, last occurence, and ks inbetween
        for i in range(len(nums)): 
            v = nums[i]
            if v == k: continue
            freq[v] += 1
            if first[v] == -1: first[v] = i
            last[v] = i

            #now calculate if removing ks is worth it
            numberOfKs = ps[last[v]+1] - ps[first[v]+1]#number of ks between first and last occurence
            net = freq[v] - numberOfKs
            if net <= 0: 
                first[v] = i
                freq[v] = 1
            res = max(res,net)

        return res + ps[-1]