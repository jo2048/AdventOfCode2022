from util import readfile
from collections import Counter


ORIENTATIONS = {
    'NW': lambda x, y: (x - 1, y - 1),
    'N': lambda x, y: (x, y - 1),
    'NE': lambda x, y: (x + 1, y - 1),
    'E': lambda x, y: (x + 1, y),
    'SE': lambda x, y: (x + 1, y + 1),
    'S': lambda x, y: (x, y + 1),
    'SW': lambda x, y: (x - 1, y + 1),
    'W': lambda x, y: (x - 1, y),
}


def move_north(x, y, elves_set):
    if all(ORIENTATIONS[k](x, y) not in elves_set for k in ('NE', 'N', 'NW')): 
        return ORIENTATIONS['N'](x, y)

def move_south(x, y, elves_set):
    if all(ORIENTATIONS[k](x, y) not in elves_set for k in ('SE', 'S', 'SW')): 
        return ORIENTATIONS['S'](x, y)

def move_east(x, y, elves_set):
    if all(ORIENTATIONS[k](x, y) not in elves_set for k in ('SE', 'E', 'NE')): 
        return ORIENTATIONS['E'](x, y)

def move_west(x, y, elves_set):
    if all(ORIENTATIONS[k](x, y) not in elves_set for k in ('SW', 'W', 'NW')): 
        return ORIENTATIONS['W'](x, y)
    

DIRECTIONS = [
    move_north,
    move_south,
    move_west,
    move_east
]


def move_elves(elves: list, round_number):
    new_pos = []
    elves_set = set(elves)

    for x, y in elves:
        if any (ORIENTATIONS[k](x, y) in elves_set for k in ORIENTATIONS):
            i = 0
            while i < 4:
                new_position = DIRECTIONS[(i + round_number) % 4](x, y, elves_set)
                if new_position is not None:
                    new_pos.append(new_position)
                    i = 15
                i += 1
            if i < 16:
                new_pos.append((x, y))   
        else:
            new_pos.append((x, y))
    
    counter = Counter(new_pos)
    for i in range(len(elves)):
        if counter[new_pos[i]] == 1:
            elves[i] = new_pos[i]


def get_bounds(elves):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = -float('inf'), -float('inf')
    for x, y in elves:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    return min_x, max_x, min_y, max_y


def day23(filepath: str, nb_rounds):
    lines = readfile(filepath)
    elves = []

    for i, line in enumerate(lines):
        for j in range(len(line)):
            if line[j] == '#':
                elves.append((j, i))

    for i in range(nb_rounds):
        new_positions = elves[:]
        move_elves(new_positions, i)
        if set(new_positions) == set(elves):
            return 'part2 : ', i + 1
        elves = new_positions

    min_x, max_x, min_y, max_y = get_bounds(elves)
    return 'part1 : ', (max_x + 1 - min_x) * (max_y + 1 - min_y) - len(elves) 


if __name__ == "__main__":
    print(day23("inputs/day23.in", 10))
    print(day23("inputs/day23.in", 10000))
