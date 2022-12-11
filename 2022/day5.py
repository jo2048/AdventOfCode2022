import re
from util import readfile


def fill_columns(line: str, columns: list) -> None:
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            columns[(i - 1) // 4].insert(0, line[i])


def parse_moves_line(line: str) -> tuple:
    line_tmp = re.sub(' |move', '', line)
    l = [int(x) for x in re.split('from|to', line_tmp)]
    l[1] -= 1
    l[2] -= 1
    return tuple(l) 
    
    
def apply_moves_part1(line: str, columns: list) -> None:
    nb_crates, start_col, end_col = parse_moves_line(line)
    for i in range(nb_crates):
        crate = columns[start_col].pop()
        columns[end_col].append(crate)
    

def apply_moves_part2(line: str, columns: list) -> None:
    nb_crates, start_col, end_col = parse_moves_line(line)
    columns[start_col], moved_crates = columns[start_col][:-nb_crates], columns[start_col][-nb_crates:]  
    columns[end_col].extend(moved_crates)


def day5(filepath: str, apply_moves_fn) -> str:
    lines = readfile(filepath, True)
    columns = [[] for _ in range(1 + (len(lines[0]) - 3) // 4)]
    
    i = 0
    while lines[i].replace(' ', '')[0] != '1':
        fill_columns(lines[i], columns)
        i += 1

    i += 2 # skip blank line
    while len(lines[i]) > 0:
        apply_moves_fn(lines[i], columns)
        i += 1 
    
    top_crates = ''
    for col in columns:
        top_crates += col[-1]
    return top_crates


if __name__ == "__main__":
    print(day5("inputs/day5.in", apply_moves_part1))
    print(day5("inputs/day5.in", apply_moves_part2))
