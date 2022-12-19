from util import readfile


POINTS = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'X' : 0,
    'Y' : 1,
    'Z' : 2
}


def compute_score_part1(p1: str, p2: str):
    x, y = POINTS[p1], POINTS[p2]
    score = y + 1
    if x == y:
        return score + 3
    elif abs(x - y) == 2:
        if x == 0:
            return score
        else:
            return score + 6
    else:
        if x > y:
            return score
    return score + 6


def compute_score_part2(p1: str, p2: str):
    x, y = POINTS[p1], POINTS[p2]
    if y == 1:
        return x + 1 + 3
    elif y == 0:
        return (x - 1) % 3 + 1
    else:
       return (x + 1) % 3 + 1 + 6    


def day2(filepath, score_function):
    lines = readfile(filepath)
    score = 0
    for line in lines:
        if line != "":
            p1, p2 = line.split(' ')
            score += score_function(p1, p2)
    return score


if __name__ == "__main__":
    print(day2("inputs/day2.in", compute_score_part1))
    print(day2("inputs/day2.in", compute_score_part2))
