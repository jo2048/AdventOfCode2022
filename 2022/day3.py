from util import readfile


def compute_score(c):
    if c.isupper():
        return ord(c.lower()) + 26 - 96
    return ord(c) - 96
    

def day3_1(filepath):
    lines = readfile(filepath)
    score = 0
    for line in lines:
        mid = len(line) // 2
        l1, l2 = line[:mid], line[mid:]
        s = set(l1) & set(l2)
        score += compute_score(s.pop())
    return score
    

def day3_2(filepath):
    lines = readfile(filepath)
    current_group = []
    score = 0
    for line in lines:
        current_group.append(set(line))
        if len(current_group) == 3:
            s = current_group[0].intersection(*current_group[1:])
            score += compute_score(s.pop())
            current_group = []
    return score


if __name__ == "__main__":
    print(day3_1("inputs/day3.in"))
    print(day3_2("inputs/day3.in"))
