from util import readfile, Position, Grid
from typing import List, Tuple


GRID_DEFAULT = '.'


class PathSector:
    def __init__(self, start: Position, end: Position):
        self.start = start
        self.end = end
        assert self.start.x == self.end.x or self.start.y == self.end.y
    
    def __iter__(self):
        self.current = self.start
        self.iter_finished = False
        return self

    def __next__(self):
        if self.iter_finished:
            raise StopIteration
        elif self.current == self.end:
            self.iter_finished = True
            return self.end
        else:
            p = Position(self.current.x, self.current.y)
            if self.current.x == self.end.x:
                if self.current.y < self.end.y:
                    self.current.y += 1
                else:
                    self.current.y -= 1
            else:
                if self.current.x < self.end.x:
                    self.current.x += 1
                else:
                    self.current.x -= 1
            return p


def find_bounds(lines: List[str]) -> Tuple[int]:
    max_x, min_x = float('-inf'), float('inf')
    max_y, min_y = float('-inf'), float('inf')
    for line in lines:
        for pos in line.split(' -> '):
            a, b = pos.split(',')
            x, y = int(a), int(b)
            max_x = max(x, max_x)
            min_x = min(x, min_x)
            max_y = max(y, max_y)
            min_y = min(y, min_y)
    return min_x, max_x, min_y, max_y


def parse_position(s: str, left_shift: int) -> Position:
    a, b = s.split(',')
    return Position(int(a) - left_shift, int(b))


def detect_walls(lines: List[str], left_shift: int=0) -> List[Position]:
    walls = []
    for line in lines:
        path = line.split(' -> ')
        i = 0
        while i < len(path) - 1:
            p1 = parse_position(path[i], left_shift)
            p2 = parse_position(path[i + 1], left_shift)
            for p in iter(PathSector(p1, p2)):
                walls.append(p)
            i += 1
    return walls


def drop(p: Position, valid_position_condition: callable):
    down_p = p.get_next_pos('D')
    for next_p in (down_p, down_p.get_next_pos('L'), down_p.get_next_pos('R')):
        if valid_position_condition(next_p):
            return next_p
    return p


def flood(
        start_p: Position, 
        valid_position_condition: callable, 
        mark_sand_fn: callable, 
        end_condition: callable):
    next_p = start_p
    p = next_p.get_next_pos('U')
    lifo = []
    i = 0
    while True:
        i += 1
        while next_p != p:
            p = next_p
            lifo.append(p)
            next_p = drop(p, valid_position_condition)
        mark_sand_fn(p)
        lifo.pop()
        next_p = lifo.pop()
        if end_condition(p):
            return i


def day14_1(filepath: str) -> int:
    lines = readfile(filepath)
    min_x, max_x, min_y, max_y = find_bounds(lines)
    grid = Grid(max_x - min_x + 3, max_y + 2, GRID_DEFAULT)
    left_shift = min_x - 1
    for wall in detect_walls(lines, left_shift):
        grid.set_value_at(wall, '#')
    
    return flood(Position(500 - left_shift, 0),
                 lambda p: grid.within_bounds(p) and grid.get_value_at(p) == GRID_DEFAULT,
                 lambda p: grid.set_value_at(p, 'o'),
                 lambda p: not grid.within_bounds(p.get_next_pos('D'))) - 1


def day14_2(filepath: str) -> int:
    lines = readfile(filepath)
    max_y = find_bounds(lines)[-1]
    d = {}
    for wall in detect_walls(lines):
        d[wall] = '#'
    
    def set_sand(p: Position):
        d[p] = 'o'

    return flood(Position(500, -2),
                 lambda p: p.y <= max_y + 1 and d.get(p) is None,
                 set_sand,
                 lambda p: p == Position(500, 0))
        

if __name__ == "__main__":
    print(day14_1("inputs/day14.in"))
    print(day14_2("inputs/day14.in"))
