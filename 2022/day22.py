from util import readfile, Position
from typing import Tuple, List


def parse_layout(lines: List[str]) -> dict:
    layout = dict()
    
    for y, line in enumerate(lines):
        min_x = float('inf')
        max_x = -1
        for i, c in enumerate(line):
            if c in '.#':
                min_x = min(i, min_x)
                max_x = max(i, max_x)
                layout[Position(i, 'min_y')] = min(y, layout.get(Position(i, 'min_y'), float('inf')))
                layout[Position(i, 'max_y')] = y
                layout[Position(i, y)] = c

        layout[Position('max_x', y)] = max_x
        layout[Position('min_x', y)] = min_x
    return layout


def parse_moves(line: str):
    moves = []
    prev_index = 0
    for i, c in enumerate(line):
        if c in 'RL':
            moves.append(int(line[prev_index:i]))
            moves.append(c)
            prev_index = i + 1
    if line[prev_index:] != '':
        moves.append(int(line[prev_index:]))
    return moves


def compute_next_pos_part1(p, layout, direction, _) -> Position:
    next_pos = p.get_next(Position.directions[direction])
    if layout.get(next_pos) is None:
        if direction == 0:
            next_pos = Position(layout[Position('max_x', p.y)], p.y)
        elif direction == 1:
            next_pos = Position(p.x, layout[Position(p.x, 'max_y')])
        elif direction == 2:
            next_pos = Position(layout[Position('min_x', p.y)], p.y)
        else:
            next_pos = Position(p.x, layout[Position(p.x, 'min_y')])
    return next_pos, direction


""" Ugly hardcoded solution for part2 that works only if the input cube is given like this:
 ##
 #
##
#
"""
def compute_next_pos_part2(p, layout, direction, dim) -> Tuple[Position, int]:
    next_pos = p.get_next(Position.directions[direction])
    new_dir = direction
    if layout.get(next_pos) is None:
        if direction == 0:
            if p.y < dim:
                next_pos = Position(0, 3 * dim - 1 - p.y)
                new_dir = 2
            elif p.y < 2 * dim:
                next_pos = Position(p.y - dim, 2 * dim)
                new_dir = 3
            elif p.y < 3 * dim:
                next_pos = Position(dim, 3 * dim - 1 - p.y)
                new_dir = 2
            else:
                next_pos = Position(p.y - 2 * dim, 0)
                new_dir = 3
        elif direction == 1:
            if p.x < dim:
                next_pos = Position(dim, p.x + dim)
                new_dir = 2
            elif p.x < 2 * dim:
                next_pos = Position(0, 2 * dim + p.x)
                new_dir = 2
            else:
                next_pos = Position(p.x - 2 * dim, 4 * dim - 1)
                new_dir = 1
        elif direction == 2:
            if p.y < dim:
                next_pos = Position(2 * dim - 1, 3 * dim - 1 - p.y)
                new_dir = 0
            elif p.y < 2 * dim:
                next_pos = Position(p.y + dim, dim - 1)
                new_dir = 1
            elif p.y < 3 * dim:
                next_pos = Position(3 * dim - 1, 3 * dim - 1 - p.y)
                new_dir = 0
            else:
                next_pos = Position(p.y - 2 * dim, 3 * dim - 1)
                new_dir = 1
        else:
            if p.x < dim:
                next_pos = Position(p.x + 2 * dim, 0)
                new_dir = 3
            elif p.x < 2 * dim:
                next_pos = Position(dim - 1, p.x + 2 * dim)
                new_dir = 0
            else:
                next_pos = Position(2 * dim - 1, p.x - dim)
                new_dir = 0
    return next_pos, new_dir


def day22(filepath: str, compute_next_pos_fn: callable) -> int:
    lines = readfile(filepath)
    layout = parse_layout(lines[:-2])
    moves = parse_moves(lines[-1])
    
    p = Position(layout[Position('min_x', 0)], 0)
    direction = 2

    # Used only for part2
    dim = (len(lines) - 2) // 4 #

    for move in moves:
        if type(move) is int:
            i = move
            while i > 0:
                next_pos, new_dir = compute_next_pos_fn(p, layout, direction, dim)
                if layout.get(next_pos) == '.':
                    p, direction = next_pos, new_dir
                elif layout.get(next_pos) == '#':
                    i = 0
                i -= 1
        else:
            if move == 'R':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
    return (p.y + 1) * 1000 + (p.x + 1) * 4 + (direction + 2) % 4


if __name__ == "__main__":
    print(day22("inputs/day22.in", compute_next_pos_part1))
    print(day22("inputs/day22.in", compute_next_pos_part2)) 
