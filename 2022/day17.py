from util import readfile, Position, Grid
from collections import defaultdict


SHAPES = (
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1))
)


def get_next_rock(i, current_y):
    x = 2
    return tuple((Position(x + 2, y + current_y) for x, y in SHAPES[i % len(SHAPES)]))


def day17(filepath: str, total_rocks: int) -> int:
    jet_pattern = readfile(filepath)[0]
    max_height = len(jet_pattern) * 4
    grid = Grid(7, max_height, '.')
    jet_index = 0
    nb_rocks = 0
    cycle_detection_dict = defaultdict(list)

    max_y = 0
    while nb_rocks < total_rocks: #len(jet_pattern) * 40:
        rock = get_next_rock(nb_rocks, max_y + 3)
        while True:
            test_rock = tuple(p.get_next(jet_pattern[jet_index % len(jet_pattern)]) for p in rock)
            jet_index += 1
            if all (0 <= p.x < 7 and grid.get_value_at(p) != '#' for p in test_rock):
                rock = test_rock

            down_rock = tuple(p.get_next('U') for p in rock)
            if not all(grid.within_bounds(p) and grid.get_value_at(p) != '#' for p in down_rock):
                break
            rock = down_rock

        max_y = max(rock[-1].y + 1, max_y)
        for p in rock:
            grid.set_value_at(p, '#')
        
        cycle_detection_dict[(nb_rocks % 5, jet_index % len(jet_pattern), rock[0].x)].append((rock[0].y, nb_rocks))
        if len(v := cycle_detection_dict[(nb_rocks % 5, jet_index % len(jet_pattern), rock[0].x)]) > 2:
            start_y, start_rock = v[0]
            diff_y = v[-1][0] - v[-2][0]
            diff_nb_rocks = v[-1][1] - v[-2][1]
            if (total_rocks - start_rock) % diff_nb_rocks == 0:
                return (total_rocks - start_rock) // diff_nb_rocks * diff_y + start_y
        nb_rocks += 1
    return max_y


if __name__ == "__main__":
    print(day17("inputs/day17.in", 2022))
    print(day17("inputs/day17.in", 1000000000000))
