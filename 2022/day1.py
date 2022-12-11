from util import readfile


def part1(filepath: str) -> int:
    lines = readfile(filepath, True)
    cnt = 0
    max_cnt = 0
    for l in lines:
        if l == "":
            max_cnt = max(max_cnt, cnt)
            cnt = 0
        else:
            cnt += int(l)
    return max_cnt
    
    
def part2(filepath: str, nb: int) -> int:
    lines = readfile(filepath, True)
    cnt = 0
    elves = []
    for l in lines:
        if l == "":
            elves.append(cnt)
            cnt = 0
        else:
            cnt += int(l)
    
    total = 0   
    for _ in range(nb):
        total += elves.pop(elves.index(max(elves)))
    return total


if __name__ == "__main__":
    print(part1("inputs/day1.in"))
    print(part2("inputs/day1.in", 3))
