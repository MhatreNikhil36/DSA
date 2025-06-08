class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.pos=(0,0)
        self.size=1
        self.moves={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
        self.food=food
        self.bounds=(height,width)
        # print('bounds',self.bounds)
        self.snake=deque()
        self.snake.append((0,0))
    def move(self, direction: str) -> int:
        x,y=self.pos
        dx,dy=self.moves[direction]
        
        nx=x+dx
        ny=y+dy
        l=self.snake.popleft()

        
        if 0<=nx<self.bounds[0] and 0<=ny<self.bounds[1] and (nx,ny) not in self.snake:
            self.pos=(nx,ny)
            if self.food and nx==self.food[0][0] and  ny==self.food[0][1]:
                if len(self.food)>1:
                    self.food=self.food[1:]
                else:
                    self.food=[]
                self.size+=1
                self.snake.appendleft(l)
                self.snake.append(self.pos)
            else:
                
                self.snake.append(self.pos)
            return self.size-1

        else:
            return -1



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)