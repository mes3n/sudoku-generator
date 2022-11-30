
from random import shuffle
from random import randint
from random import choice


class Generator:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solutions = 0

    def generate_solution(self):
        self.solve(create=True)

    def solve(self, create=False, limit=100):
        for y, row in enumerate(self.board):
            for x, num in enumerate(row):
                if num == 0:
                    for i in self.valid_values(x, y, create):  # this decides if it solves or generates
                        self.board[y][x] = i
                        if self.solve():
                            return True

                    self.board[y][x] = 0
                    return False
        
        if create:
            return True
        else:
            self.solutions += 1
            return False if self.solutions < limit else True  # exit if more than 100 solutions have been found

    def valid_values(self, x, y, create) -> list[int]:
        result = list(range(1, 10))
        if create: shuffle(result)

        for num in self.board[y]:
            if num in result:
                result.remove(num)

        for num in (self.board[i][x] for i in range(0, 9)):
            if num in result:
                result.remove(num)
        
        x = (x // 3) * 3
        y = (y // 3) * 3

        for i in range(0, 3):
            for num in self.board[y + i][x:x + 3]:
                if num in result:
                    result.remove(num)

        return result
    
    def count_solutions(self, limit=100):
        self.solutions = 0
        self.solve(limit=limit)
        return self.solutions

    def count_values(self):
        count = 0
        for row in self.board:
            for num in row:
                if num != 0:
                    count += 1
        return count

    def set_remainder(self, num):
        constants = []
        while self.count_values() > num:
            # get all positions with a value
            positions = []
            for y, row in enumerate(self.board):
                for x, num in enumerate(row):
                    if num != 0 and (x, y) not in constants:
                        positions.append((x, y, num))

            if not len(positions):
                return

            shuffle(positions)

            for x, y, num in positions:
                self.board[y][x] = 0

                if self.count_solutions(limit=2) > 1:
                    self.board[y][x] = num
                    constants.append((x, y))
            
                self.display_board()
                print(self.count_values())
                

    def display_board(self, name=''):
        print(name)
        for y, row in enumerate(self.board):
            if y % 3 == 0 and y != 0:
                print('- - - + - - - + - - -')
            for x, num in enumerate(row):
                if x % 3 == 0 and x != 0:
                    print('|', end=' ')
                print(num, end=' ')
            print()
        print()


def main():
    generator = Generator()

    generator.generate_solution()
    generator.display_board('solution')

    generator.set_remainder(20)
    generator.display_board('problem')


if __name__ == '__main__':
    main()

