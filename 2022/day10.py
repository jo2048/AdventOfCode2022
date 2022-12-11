from typing import Tuple, Callable
from util import readfile


def increment_cycle_part1(cycle, register_value, result) -> Tuple[int]:
    cycle += 1
    if (cycle + 20) % 40 == 0:
        if result is None:
            result = 0
        result += cycle * register_value
    return cycle, result


def increment_cycle_part2(cycle, register_value, result) -> Tuple[int, str]:
    cycle += 1
    if result is None:
        result = ''
    result += '#' if abs((cycle - 1) % 40 - register_value) <= 1 else '.'
    if cycle % 40 == 0:
        result += '\n'
    return cycle, result


def day10(filepath: str, increment_cycle_fn: Callable):
    cycle = 0
    register_value = 1
    result = None

    for line in readfile(filepath):
        cycle, result = increment_cycle_fn(cycle, register_value, result)
        if line != 'noop':
            value = int(line.split(' ')[1])
            cycle, result = increment_cycle_fn(cycle, register_value, result)
            register_value += value
        if cycle > 240:
            break
        
    return result


if __name__ == "__main__":
    print(day10("inputs/day10.in", increment_cycle_part1))
    print(day10("inputs/day10.in", increment_cycle_part2))
