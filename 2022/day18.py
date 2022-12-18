from util import readfile
import operator


def get_neighbors(triplet):
    sides = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]
    return [tuple(map(operator.add, triplet, side)) for side in sides]


def load_input(filepath: str) -> set:
    lines = readfile(filepath)
    points = set()
    for line in lines:
        x, y, z = (int(c) for c in line.split(','))
        points.add((x, y, z))
    return points


def day18_1(filepath: str) -> int:
    lava = load_input(filepath)
    
    exposed_sides = 0
    for p in list(lava):
        v = 6
        for neighbor in get_neighbors(p):
            if neighbor in lava:
                v -= 1
        exposed_sides += v
    return exposed_sides


def get_bounds(lava: set):
    max_x, max_y, max_z = 0, 0, 0
    for x, y, z in list(lava):
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)
    return max_x + 1, max_y + 1, max_z + 1


def within_bounds(p, bounds):
    return all (-1 <= p[i] <= bounds[i] for i in range(3))


def dfs(p, marked_points: set, lava: set, bounds):
    for side in get_neighbors(p):
        if within_bounds(p, bounds) and not (side in lava or side in marked_points):
            marked_points.add(side)
            dfs(side, marked_points, lava, bounds) 


def day18_2(filepath: str) -> int:
    lava = load_input(filepath)
    
    bounds = get_bounds(lava)
    marked_points = set()
    dfs(bounds, marked_points, lava, bounds)
    
    exposed_sides = 0
    for p in list(lava):
        v = 6
        for neighbor in get_neighbors(p):
            if neighbor not in marked_points:
                v -= 1
        exposed_sides += v
    return exposed_sides


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(8000)
    print(day18_1("inputs/day18.in"))
    print(day18_2("inputs/day18.in"))
