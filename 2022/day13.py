from util import readfile
import functools


def check(left_side, right_side) -> int:
    if type(left_side) is list and type(right_side) is list:
        for i in range(min(len(left_side), len(right_side))):
            v = check(left_side[i], right_side[i]) 
            if v != 0:
                return v
        return len(right_side) -  len(left_side)
    elif type(left_side) is int and type(right_side) is int:
        return right_side - left_side
    else:
        if type(left_side) is list:
            return check(left_side, [right_side])
        else:
            return check([left_side], right_side)


def day13_1(filepath: str) -> int:
    lines = readfile(filepath)
    i = 0
    result = 0
    while i * 3 < len(lines):
        if check(eval(lines[i * 3]), eval(lines[i * 3 + 1])) > 0:
            result += i + 1
        i += 1
    return result


def day13_2(filepath: str) -> int:
    data = list(map(eval, filter(lambda x: x != '', readfile(filepath))))
    data.append([[2]])
    data.append([[6]])
    data.sort(key=functools.cmp_to_key(check), reverse=True)
    data = list(map(str, data))

    return (data.index('[[2]]') + 1) *  (data.index('[[6]]') + 1) 
    

if __name__ == "__main__":
    print(day13_1("inputs/day13.in"))
    print(day13_2("inputs/day13.in"))

