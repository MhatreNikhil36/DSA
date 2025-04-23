class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        paper=[[0,0,0] for i in range(3)]
        print(paper)
        for i,x in enumerate(moves):
            val='B'
            if i%2==0:
                val='A'
            paper[x[0]][x[1]]=val

        posible={'up':[(-1,0),(-2,0)],'down':[(1,0),(2,0)],'left':[(0,1),(0,2)],'right':[(0,-1),(0,-2)],'cross1':[(-1,-1),(1,1)],'cross2':[(-1,1),(1,-1)]}
        def checkWin(i,j):
            for d in posible:
                c=0
                for x,y in posible[d]:
                    if 0<=i+x<3 and 0<=j+y<3 and paper[i+x][j+y]==paper[i][j]:
                        c+=1
                if c==2:
                    return paper[i][j]
            return False
        
        for i in range(3):
            for j in range(3):
                x=checkWin(i,j)
                if x:
                    return x
        if len(moves)<9:
            return "Pending"
        return "Draw" 