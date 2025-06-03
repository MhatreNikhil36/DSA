class TicTacToe:

    def __init__(self, n: int):
        self.board = [[None for _ in range(n)] for _ in range(n)]
        self.n = n
        self.op = {
            0: {(1, 0), (-1, 0)},   # Vertical directions
            1: {(0, 1), (0, -1)},   # Horizontal directions
            2: {(-1, 1), (1, -1)},  # Diagonal directions
            3: {(-1, -1), (1, 1)}   # Diagonal directions
        }

    def check(self, i, j, player):
        for d in self.op:
            c = -1
            for dx, dy in self.op[d]:
                x, y = i, j
                
                while 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == player:
                    x += dx
                    y += dy
                    c += 1
                # print(d,c)
                if c == self.n:
                    return player
        return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        # for x in self.board:
        #     print(x)
        a = self.check(row, col, player)
        # print(a)
        return a
