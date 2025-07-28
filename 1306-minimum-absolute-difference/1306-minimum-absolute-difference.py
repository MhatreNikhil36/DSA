class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        diffMap={}
        heapq.heapify(arr)
        lower=heapq.heappop(arr)
        minDiff=math.inf
        while arr:
            upper=heapq.heappop(arr)
            diff=upper-lower
            if  diff in diffMap:
                diffMap[diff].append([lower,upper])
            else:
                diffMap[diff]=[[lower,upper]]
            if  minDiff>diff:
                minDiff=diff
            lower=upper
        return diffMap[minDiff]
            