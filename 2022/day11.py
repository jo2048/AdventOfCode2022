from util import readfile
from typing import List, Callable
from math import lcm


class Item:
    decrease_worry_fn: Callable = None

    def __init__(self, worry_level: int):
        self.worry_level = worry_level
    
    def decrease_worry_level(self):
        self.worry_level = Item.decrease_worry_fn(self.worry_level)


class Monkey:
    def __init__(self, monkeys: list, items: List[Item], inspection_fn: Callable, divisor: int, true_destination: int, false_destination: int):
        self.monkeys = monkeys
        self.inspection_fn = inspection_fn
        self.divisor = divisor
        self.true_destination = true_destination
        self.false_destination = false_destination
        self.items = items

        self.inspection_cnt = 0

    def add_item(self, item: Item):
        self.items.append(item)

    def inspect_items(self):
        while len(self.items) > 0:
            item = self.items.pop()
            self.inspection_cnt += 1
            item.worry_level = self.inspection_fn(item.worry_level)
            item.decrease_worry_level()
            if item.worry_level % self.divisor == 0:
                self.monkeys[self.true_destination].add_item(item)
            else:
                self.monkeys[self.false_destination].add_item(item)


def parse_int(s: str) -> int:
    return int(s.split(' ')[-1])


def parse_line_bloc(bloc: List[str]) -> tuple:
    items = [Item(int(x)) for x in bloc[0].split(': ')[-1].split(', ')]
    op = bloc[1].split('= ')[1]
    inspection_fn = lambda old : eval(op)
    divisor = parse_int(bloc[2])
    true_destination = parse_int(bloc[3])
    false_destination = parse_int(bloc[4])
    return items, inspection_fn, divisor, true_destination, false_destination


def day11(filepath: str, nb_rounds: int, part1: bool) -> int:
    lines = readfile(filepath)
    monkeys = []
    i = 0

    while i < len(lines):
        monkeys.append(Monkey(monkeys, *parse_line_bloc(lines[i+1: i+6])))
        i += 7
    
    if part1:
        Item.decrease_worry_fn = lambda x : x // 3
    else:
        constant = lcm(*[monkey.divisor for monkey in monkeys])
        Item.decrease_worry_fn = lambda x : x - (x // constant) * constant if x > constant else x
    
    for _ in range(nb_rounds):
        for monkey in monkeys:
            monkey.inspect_items()

    counts = sorted([monkey.inspection_cnt for monkey in monkeys])
    return counts[-1] * counts[-2]


if __name__ == "__main__":
    print(day11("inputs/day11.in", 20, True))
    print(day11("inputs/day11.in", 10000, False))
