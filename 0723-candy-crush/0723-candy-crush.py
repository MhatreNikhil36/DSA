
import copy
class Solution:

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        crush=[]
        seen=set()
        n=len(board)
        m=len(board[0])
        senarios={((1,0),(-1,0)),((1,0),(2,0)),((-1,0),(-2,0)),((0,1),(0,-1)),((0,1),(0,2)),((0,-1),(0,-2))}

        def identify(i,j):
            nonlocal crush
            val=board[i][j]
            for a,b in senarios:
                x1,y1=i+a[0],j+a[1]
                x2,y2=i+b[0],j+b[1]
                if 0<=x1<n and 0<=x2<n and 0<=y1<m and 0<=y2<m:
                    # print(i,j,x1,y1,x2,y2,val,board[x1][y1],board[x2][y2])
                    if val==board[x1][y1] and val==board[x2][y2]:
                        crush.append((i,j))
                        # print(i,j)
                        break
            return
        def gravity(x,y):
            if board[x][y]!=0:
                return
            c=x
            while c>=0 and board[c][y]==0:
                c-=1
            if board[c][y]!=0:
                while c>=0 and board[c][y]!=0:
                    board[x][y]=board[c][y]
                    board[c][y]=0
                    c-=1
                    x-=1
            return
            
     
        prev=None
        while prev!=board:
            prev=copy.deepcopy(board)
            for i in range(n):
                for j in range(m):
                    identify(i,j)
            print(crush)
            for x,y in crush:
                board[x][y]=0
            for x,y in crush:
                gravity(x,y)
            crush=[]
            print(board==prev)
        return board

        
            
            
