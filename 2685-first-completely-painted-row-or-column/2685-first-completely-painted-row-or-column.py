class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # c=dict()
        m=len(mat)
        n=len(mat[0])
        matmap=dict()
        for i in range(len(mat)):
            for  j in range(len(mat[0])):
                matmap[mat[i][j]]=(i,j)
        # print('\n\n',matmap,'\n\n')

        row = [0] * m
        col = [0] * n
        for i in range(len(arr)):
            x = matmap[arr[i]]
            row[x[0]] += 1
            col[x[1]] += 1
            if row[x[0]] == n or col[x[1]] == m:
                return i
        return -1
        # for i in range(len(arr)):
        #     print(i,c)
        #     pos=matmap[arr[i]]
        #     if (pos[0],0) in c:
        #         c[(pos[0],-1)]+=1
        #     else:
        #         c[(pos[0],-1)]=1
        #     if ((-1,pos[1])) in c:
        #         c[(-1,pos[1])]+=1
        #     else:
        #         c[(-1,pos[1])]=1
        #     print(i,c)
        #     if c[(pos[0],-1)]==n or c[(-1,pos[1])]==m:
        #         return i
        # return 1

        