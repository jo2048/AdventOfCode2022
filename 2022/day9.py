from typing import List
from util import readfile, Position


class Rope(Position):
    def __init__(self, x: int=0, y: int=0, tail=None):
        Position.__init__(self, x, y)
        self.tail = tail
    
    def apply_move(self, direction):
        p = self.get_next(direction)
        self.x, self.y = p.x, p.y
        self.move_tail()

    def move_tail(self):
        if self.tail is not None:
            if abs(self.x - self.tail.x) > 1 or abs(self.y - self.tail.y) > 1:
                if self.y == self.tail.y:
                    if self.x < self.tail.x:
                        self.tail.x -= 1
                    else:
                        self.tail.x += 1
                if self.x == self.tail.x:
                    if self.y < self.tail.y:
                        self.tail.y -= 1
                    else:
                        self.tail.y += 1
                else:
                    if self.x < self.tail.x and self.y < self.tail.y:
                        self.tail.x -= 1
                        self.tail.y -= 1
                    elif self.x > self.tail.x and self.y < self.tail.y:
                        self.tail.x += 1
                        self.tail.y -= 1
                    elif self.x < self.tail.x and self.y > self.tail.y:
                        self.tail.x -= 1
                        self.tail.y += 1
                    elif self.x > self.tail.x and self.y > self.tail.y:
                        self.tail.x += 1
                        self.tail.y += 1
                self.tail.move_tail()

    def __str__(self):
        s = f'x = {self.x}, y = {self.y}'
        if self.tail is not None:
            s += ' -> ' + str(self.tail)
        return s


def load_moves_list(filepath: str) -> List[str]:
    moves = []
    for line in readfile(filepath):
        if line != '':
            move, nb_moves = line.split(' ')
            moves.extend([move] * int(nb_moves))
    return moves


def day9(filepath, nb_ropes):
    moves = load_moves_list(filepath)
    tail = Rope()
    head = Rope(tail=tail)
    s = set()
    s.add((0, 0))

    for _ in range(nb_ropes - 2):
        head = Rope(tail=head)

    for move in moves:
        head.apply_move(move)
        s.add((tail.x, tail.y))
    return len(s)


if __name__ == "__main__":
    print(day9("inputs/day9.in", 2))
    print(day9("inputs/day9.in", 10))
