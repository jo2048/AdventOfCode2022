from util import readfile


def get_range(s: str):
    start, end = s.split('-')
    return int(start), int(end)


part1_score_fn = lambda x1, y1, x2, y2: (x1 <= x2 and y1 >= y2) or (x2 <= x1 and y2 >= y1)
part2_score_fn = lambda x1, y1, x2, y2: not ((x1 < x2 and y1 < x2) or x1 > y2)


def day4(filepath: str, score_function) -> int:
    cnt = 0
    for line in readfile(filepath):
        l1, l2 = line.split(',')
        if score_function(*get_range(l1), *get_range(l2)):
            cnt += 1 
    return cnt


if __name__ == "__main__":
    print(day4("inputs/day4.in", part1_score_fn))
    print(day4("inputs/day4.in", part2_score_fn))
