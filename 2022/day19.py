from util import readfile
from typing import Tuple
import re
import operator
import time


LINE_FORMAT = re.compile(r'Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')
RESOURCES = ('ore', 'clay', 'obsidian', 'geode')


def load_blueprints(filepath: str) -> Tuple[tuple]:
    lines = readfile(filepath)
    blueprints = []
    for line in lines:
        ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = (int(x) for x in LINE_FORMAT.findall(line)[0])
        blueprints.append(((ore_ore, 0, 0, 0), (clay_ore, 0, 0, 0), (obsidian_ore, obsidian_clay, 0, 0), (geode_ore, 0, geode_obsidian, 0)))
    return blueprints


def tuple_add(t1, t2):
    return tuple(map(operator.add, t1, t2))


def tuple_sub(t1, t2):
    return tuple(map(operator.sub, t1, t2))


T = dict()


def init_T(v):
    for i in range (v + 1):
        T[i] = i * (i + 1) // 2


def eval_blueprint(blueprint, nb_minutes):
    robots = (1, 0, 0, 0)
    max_robots = tuple(max(cost[i] for cost in blueprint) for i in range(3))
    stock = (0, 0, 0, 0)
    total_time = nb_minutes
    states = [(robots, stock, nb_minutes, (,))]
    max_geodes = 0
    current_max = 0
    while len(states) > 0:
        robots, stock, nb_minutes, not_build = states.pop()
        # print(robots, stock, nb_minutes, len(states), sep=' - ')
        if nb_minutes == 0:
            max_geodes = max(stock[3], max_geodes)
        # Not enough obsidian to build a new geode robot before the end
        elif stock[2] + robots[2] * nb_minutes + T[nb_minutes] < blueprint[3][2]:
            max_geodes = max(stock[3] + nb_minutes * robots[3], max_geodes)
            # print(robots, stock, nb_minutes, sep=' - ')
        elif stock[3] + nb_minutes * robots[3] + T[nb_minutes] < current_max:
            pass
        else:
            new_stock = tuple_add(stock, robots)
            if stock[2] >= blueprint[3][2] and stock[0] >= blueprint[3][0]:
                current_max = max(stock[3] + robots[3] + (robots[3] + 1) * (nb_minutes - 1), current_max)
                states.append((tuple_add(robots, (0, 0, 0, 1)), 
                               tuple_sub(new_stock, blueprint[3]), 
                               nb_minutes - 1,
                               (,)))
            else:
                builded = 0
                if stock[0] >= blueprint[0][0] and robots[0] < max_robots[0] and robots[0] * nb_minutes + stock[0] < max_robots[0] * nb_minutes and 
                    0 not in not_build:
                    builded = 1
                    states.append((tuple_add(robots, (1, 0, 0, 0)), 
                                  tuple_sub(new_stock, blueprint[0]), 
                                  nb_minutes - 1),
                                  (,))
                if stock[0] >= blueprint[1][0] and robots[1] < max_robots[1] and robots[1] * nb_minutes + stock[1] < max_robots[1] * nb_minutes:
                    builded += 1
                    states.append((tuple_add(robots, (0, 1, 0, 0)), 
                                  tuple_sub(new_stock, blueprint[1]), 
                                  nb_minutes - 1),
                                  (,))
                if stock[0] >= blueprint[2][0] and stock[1] >= blueprint[2][1] and robots[2] < max_robots[2] and robots[2] * nb_minutes + stock[2] < max_robots[2] * nb_minutes:
                    builded += 1
                    states.append((tuple_add(robots, (0, 0, 1, 0)), 
                                  tuple_sub(new_stock, blueprint[2]), 
                                  nb_minutes - 1),
                                  (,))
                if builded < 3:
                    states.append((robots, new_stock, nb_minutes - 1))
    return max_geodes


def day19(filepath: str) -> int:
    nb_minutes = 24
    init_T(nb_minutes)
    blueprints = load_blueprints(filepath)
    total = 0
    for i, blueprint in enumerate(blueprints):
        t = time.time()
        v = eval_blueprint(blueprint, nb_minutes)
        print(i + 1, v, time.time() - t, sep=" - ")
        total += (i + 1) * v
    return total
    

if __name__ == "__main__":
    print(day19("test.in"))
    # print(day19("inputs/day19.in"))

# 1625 too low 