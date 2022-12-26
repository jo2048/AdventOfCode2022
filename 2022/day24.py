from util import readfile, Position, Grid
from math import lcm


class EvolutiveBoard:
    def __init__(self, filepath: str):
        lines = readfile(filepath)
        self.width = len(lines[0]) - 2
        self.height = len(lines) - 2

        self.period = lcm(self.width, self.height)
        self.initial_grid = Grid(self.width, self.height, '.')
        for i, line in enumerate(lines[1:-1]):
            for j in range(self.width):
                if line[j + 1] in '><^v':
                    self.initial_grid.set_value_at(Position(j, i), line[j + 1])
        self.grids = []
        for i in range(self.period):
            self.grids.append(self._compute_grid(i))

    def get_grid(self, nb_minutes: int) -> Grid:
        return self.grids[nb_minutes % self.period]
    
    def _compute_grid(self, nb_minutes) -> Grid:
        grid = Grid(self.width, self.height, 0)
        for i in range(self.width):
            for j in range(self.height):
                if self.initial_grid.get_value_at(Position((i - nb_minutes) % self.width, j)) == ">" \
                   or self.initial_grid.get_value_at(Position((i + nb_minutes) % self.width, j)) == "<" \
                   or self.initial_grid.get_value_at(Position(i, (j - nb_minutes) % self.height)) == "v" \
                   or self.initial_grid.get_value_at(Position(i, (j + nb_minutes) % self.height)) == "^":
                    grid.set_value_at(Position(i, j), 1)
        return grid


def solve(board: EvolutiveBoard, start: Position, end: Position, start_time: int) -> int: 
    states = set([start])
    nb_minutes = start_time

    while len(states) > 0:
        next_states = set()
        grid = board.get_grid(nb_minutes + 1)

        for p in states:
            for next_p in p.get_neighors():
                if next_p == end:
                    return nb_minutes + 1
                elif grid.within_bounds(next_p) and grid.get_value_at(next_p) == 0:
                    next_states.add(next_p)
            if grid.within_bounds(p) and grid.get_value_at(p) == 0:
                next_states.add(p)
        states = next_states
        if not states:
            states.add(start)
        nb_minutes += 1
    return None


if __name__ == "__main__":
    board = EvolutiveBoard("inputs/day24.in")
    start = Position(0, -1)
    end = Position(board.width - 1, board.height)
    part1 = solve(board, start, end, 1)
    print(f"Part 1 : {part1}")
    print(f"Part 2 : {solve(board, start, end, solve(board, end, start, part1))}")
