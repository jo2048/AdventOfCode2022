from __future__ import annotations
from typing import Tuple, List


def readfile(filepath: str, keep_last_empty_line: bool=False) -> list:
    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()
    if not keep_last_empty_line and lines[-1] == '\n':
        lines.pop()
    return [l.strip('\n') for l in lines]
    

class Position:
    directions = ['L', 'U', 'R', 'D']

    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y

    def get_next(self, direction: str) -> Position:
        if direction in ('L', '<'):
            return Position(self.x - 1, self.y)
        elif direction in ('R', '>'):
            return Position(self.x + 1, self.y)
        elif direction == 'U':
            return Position(self.x, self.y - 1)
        else:   
            return Position(self.x, self.y + 1)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'(x = {self.x} ;y = {self.y})'


class Grid:
    def __init__(self, width: int, height: int, init_value=None):
        self.width = width
        self.height = height
        self.cells = [[init_value] * width for _ in range(height)]

    def within_bounds(self, p: Position) -> bool:
        return 0 <= p.x < self.width and 0 <= p.y < self.height

    def get_value_at(self, p: Position):
        return self.cells[p.y][p.x]

    def set_value_at(self, p: Position, value):
        self.cells[p.y][p.x] = value

    def __str__(self):
        s = ''
        for line in self.cells:
            s += ''.join(map(str, line)) + '\n'
        return s

    @staticmethod
    def init_from_str_list(lines: List[str]) -> Grid:
        grid = Grid(len(lines[0]), len(lines))
        for i, line in enumerate(lines):
            grid.cells[i] = line
        return grid

