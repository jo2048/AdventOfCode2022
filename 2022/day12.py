from util import readfile, Position
from typing import Tuple, List


def load_grid(filepath: str) -> Tuple[List, Position, Position]:
    lines = readfile(filepath)
    grid = [[] for _ in range(len(lines))]
    start = None
    end = None
    low_points = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'S':
                start = Position(i, j)
                low_points.append(start)
                grid[i].append(1)
            elif c == 'E':
                end = Position(i, j)
                grid[i].append(26)
            else:
                grid[i].append(ord(c) - 96)
                if c == 'a':
                    low_points.append(Position(i, j))
    return grid, start, end, low_points


def set_cost_r(grid, costs, position, cost):
    costs[position.x][position.y] = cost 
    height = grid[position.x][position.y]
    for direction in Position.directions:
        next_pos = Position(*Position.get_next_pos(position.x, position.y, direction))
        if (0 <= next_pos.x < len(grid) and 
            0 <= next_pos.y < len(grid[0]) and
            grid[next_pos.x][next_pos.y] <= height + 1 and
            costs[next_pos.x][next_pos.y] > cost + 1):
            set_cost_r(grid, costs, next_pos, cost + 1)


def day12_1(filepath: str) -> int:
    grid, start, end, _ = load_grid(filepath)
    costs = [[float('inf')]* len(grid[0]) for _ in range(len(grid))]
    set_cost_r(grid, costs, start, 0)
    return costs[end.x][end.y]


def day12_2(filepath: str) -> int:
    grid, start, end, low_points = load_grid(filepath)
    costs = [[float('inf')]* len(grid[0]) for _ in range(len(grid))]
    for p in low_points:
        set_cost_r(grid, costs, p, 0)
    return costs[end.x][end.y]


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(2000)
    print(day12_1("inputs/day12.in"))
    print(day12_2("inputs/day12.in"))
