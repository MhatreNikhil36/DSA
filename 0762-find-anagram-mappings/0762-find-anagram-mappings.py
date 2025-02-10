class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map=dict()

        for i in range(len(nums2)):
            map[nums2[i]]=i
        ans=[]
        for x in nums1:
            ans.append(map[x])
        return ans 
        