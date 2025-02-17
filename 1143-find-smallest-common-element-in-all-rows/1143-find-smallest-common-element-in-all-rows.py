class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        prev=None
        for x in range(len(mat)):
            if  x==0:
                prev=set(mat[x])
                continue
            if len(prev)==0:
                return -1
            # print(prev)
            curr=set()
            for i in mat[x]:
                if i in prev:
                    curr.add(i)
            
            prev=curr
            # print(prev)
        return min(prev) if len(prev)>0 else -1


        