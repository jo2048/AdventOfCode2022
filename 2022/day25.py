from util import readfile


SNAFU_DICT = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
    -2: '=',
    -1: '-',
    0: '0'
}


def snafu_to_base10(s: str) -> int:
    nb = 0
    for i, c in enumerate(s):
        nb += SNAFU_DICT[c] * pow(5, len(s) - 1 - i)
    return nb


def base10_to_snafu(x: int) -> str:
    r_base5 = base10_to_reverse_base5(x)
    result = ''
    report = 0
    for c in r_base5:
        v = int(c)
        if v + report < 3:
            result += str(v + report)
            report = 0
        else:
            result += SNAFU_DICT[v + report - 5]
            report = 1
    if report > 0:
        result += str(report)
    return result[::-1]


def base10_to_reverse_base5(x: int) -> str:
    s = ''
    if x == 0:
        return '0'
    while x > 0:
        x, r = divmod(x, 5)
        s += str(r)
    return s


def day25(filepath: str) -> int:
    lines = readfile(filepath)
    total = sum(snafu_to_base10(line) for line in lines)
    return base10_to_snafu(total)


if __name__ == "__main__":
    print(day25("test/day25.in"))
    print(day25("inputs/day25.in"))
