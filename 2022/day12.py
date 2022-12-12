from util import readfile, Position, Grid
from typing import Tuple, List


def load_grid(filepath: str) -> Tuple[List, Position, Position]:
    lines = readfile(filepath)
    grid = Grid(len(lines[0]), len(lines))
    start = None
    end = None
    low_points = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'S':
                start = Position(i, j)
                low_points.append(start)
                grid.set_value_at(Position(i, j), 1)
            elif c == 'E':
                end = Position(i, j)
                grid.set_value_at(Position(i, j), 26)
            else:
                grid.set_value_at(Position(i, j), ord(c) - 96)
                if c == 'a':
                    low_points.append(Position(i, j))
    return grid, start, end, low_points


def set_cost_r(grid: Grid, costs: Grid, p: Position, cost: int):
    costs.set_value_at(p, cost)
    height = grid.get_value_at(p)
    for direction in Position.directions:
        next_pos = p.get_next_pos(direction)
        if (grid.within_bounds(next_pos) and
            grid.get_value_at(next_pos) <= height + 1 and
            costs.get_value_at(next_pos) > cost + 1):
            set_cost_r(grid, costs, next_pos, cost + 1)


def day12_1(filepath: str) -> int:
    grid, start, end, _ = load_grid(filepath)
    costs = Grid(grid.width, grid.height, float('inf'))
    set_cost_r(grid, costs, start, 0)
    return costs.get_value_at(end)


def day12_2(filepath: str) -> int:
    grid, start, end, low_points = load_grid(filepath)
    costs = Grid(grid.width, grid.height, float('inf'))
    for p in low_points:
        set_cost_r(grid, costs, p, 0)
    return costs.get_value_at(end)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(2000)
    print(day12_1("inputs/day12.in"))
    print(day12_2("inputs/day12.in"))
