from util import readfile


def day6(filepath: str, nb_consecutive_char: int) -> int:
    for line in readfile(filepath):
        for i in range(nb_consecutive_char, len(line)):
            if len(set(line[i-nb_consecutive_char:i])) == nb_consecutive_char:
                return i


if __name__ == "__main__":
    print(day6("inputs/day6.in", 4))
    print(day6("inputs/day6.in", 14))
