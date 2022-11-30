board = [

    [9, 0, 0,   0, 1, 0,    0, 0, 6],
    [2, 0, 0,   5, 0, 6,    3, 0, 0],
    [0, 5, 0,   0, 4, 0,    0, 0, 0],

    [0, 2, 0,   7, 0, 9,    0, 0, 4],
    [3, 0, 0,   0, 0, 0,    0, 8, 0],
    [0, 0, 0,   0, 5, 0,    0, 0, 0],  #     [0, 0, 0,   0, 5, 0,    0, 0, 0],

    [0, 0, 0,   0, 0, 1,    0, 0, 0],
    [0, 7, 0,   6, 0, 2,    0, 0, 9],
    [0, 0, 9,   0, 0, 0,    4, 0, 0],

]

board = [

    [0, 2, 6,   3, 5, 0,    0, 0, 1],
    [8, 0, 1,   0, 6, 0,    0, 0, 0],
    [0, 0, 0,   8, 1, 9,    5, 0, 6],

    [3, 0, 2,   0, 0, 0,    1, 0, 5],
    [5, 0, 0,   9, 0, 0,    0, 0, 0],
    [0, 9, 0,   2, 4, 0,    8, 6, 3],  #     [0, 0, 0,   0, 5, 0,    0, 0, 0],

    [0, 0, 5,   4, 9, 7,    0, 0, 0],
    [0, 3, 4,   1, 2, 0,    9, 5, 0],
    [0, 0, 0,   5, 8, 0,    0, 7, 0],

]


class Solver:
    def __init__(self, board):
        self.board = board
        self.solutions = 0


    def solve(self):
        for y, row in enumerate(self.board):
            for x, num in enumerate(row):
                if num == 0:
                    for i in range(1, 10):
                        if self.validate(i, x, y):
                            self.board[y][x] = i
                            if self.solve():
                                return True

                    self.board[y][x] = 0
                    return False
        
        self.solutions += 1
        return False if self.solutions < 100 else True  # stop counting after 100 solutions


    def count_solutions(self):
        self.solve()
        return self.solutions


    def validate(self, num, x, y):
        if num in self.board[y]:
            return False

        if num in (self.board[i][x] for i in range(0, 9)):
            return False
        
        x = (x // 3) * 3
        y = (y // 3) * 3

        for i in range(0, 3):
            if num in self.board[y + i][x:x+3]:
                return False

        return True


    def display(self):
        for y, row in enumerate(board):
            if y % 3 == 0 and y != 0:
                print('- - - + - - - + - - -')
            for x, num in enumerate(row):
                if x % 3 == 0 and x != 0:
                    print('|', end=' ')
                print(num, end=' ')
            print()
        print()


def main():
    solver = Solver(board)
    print(solver.count_solutions())
    solver.display()


if __name__ == '__main__':
    main()
