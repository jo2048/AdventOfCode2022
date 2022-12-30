from util import readfile, Position, Grid


def load_grid(filepath: str) -> Grid:
    lines = readfile(filepath)
    return Grid.init_from_str_list([line[1:-1] for line in lines[1:-1]])


def is_valid_position(grid: Grid, p: Position, time: int):
    return grid.within_bounds(p) \
        and grid.get_value_at(Position((p.x - time) % grid.width, p.y)) != ">" \
        and grid.get_value_at(Position((p.x + time) % grid.width, p.y)) != "<" \
        and grid.get_value_at(Position(p.x, (p.y - time) % grid.height)) != "v" \
        and grid.get_value_at(Position(p.x, (p.y + time) % grid.height)) != "^"


def solve(grid: Grid, start: Position, end: Position, start_time: int) -> int: 
    states = set([start])
    nb_minutes = start_time

    while len(states) > 0:
        next_states = set()

        for p in states:
            for next_p in p.get_neighors():
                if next_p == end:
                    return nb_minutes + 1
                elif is_valid_position(grid, next_p, nb_minutes):
                    next_states.add(next_p)
            if is_valid_position(grid, p, nb_minutes):
                next_states.add(p)
        states = next_states
        if not states:
            states.add(start)
        nb_minutes += 1
    return None


if __name__ == "__main__":
    grid = load_grid("inputs/day24.in")
    start = Position(0, -1)
    end = Position(grid.width - 1, grid.height)
    part1 = solve(grid, start, end, 1)
    print(part1)
    print(solve(grid, start, end, solve(grid, end, start, part1)))
