from util import readfile
from typing import Tuple
import collections
import re
import math
import operator
import time


LINE_FORMAT = re.compile(r'Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')


Resources = collections.namedtuple("Resources", "ore, clay, obsidian, geode")


def load_blueprints(filepath: str) -> Tuple[tuple]:
    lines = readfile(filepath)
    blueprints = []
    for line in lines:
        ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = (int(x) for x in LINE_FORMAT.findall(line)[0])
        blueprints.append(Resources(
            Resources(ore_ore, 0, 0, 0), 
            Resources(clay_ore, 0, 0, 0), 
            Resources(obsidian_ore, obsidian_clay, 0, 0), 
            Resources(geode_ore, 0, geode_obsidian, 0)))
    return blueprints


def resources_add(t1, t2):
    return Resources(*tuple(map(operator.add, t1, t2)))


def resources_sub(t1, t2):
    return Resources(*tuple(map(operator.sub, t1, t2)))


T = dict()


def init_T(v):
    for i in range (v + 1):
        T[i] = i * (i + 1) // 2


def eval_blueprint(blueprint, nb_minutes):
    max_robots = Resources(*tuple(max(cost[i] for cost in blueprint) for i in range(3)), 0) 

    robots = Resources(1, 0, 0, 0)
    stock = Resources(0, 0, 0, 0)
    states = [(robots, stock, nb_minutes, None)]
    
    max_geodes = 0
    while len(states) > 0:
        robots, stock, nb_minutes, last = states.pop()
        if nb_minutes == 0:
            max_geodes = max(stock.geode, max_geodes)
        elif stock.obsidian + robots.obsidian * nb_minutes + T[nb_minutes] < blueprint.geode.obsidian:
            max_geodes = max(stock.geode + nb_minutes * robots.geode, max_geodes)

        elif max_geodes - stock.geode >= (nb_minutes * (2 * robots.geode + nb_minutes - 1)) // 2:
            pass
        else:
            new_stock = resources_add(stock, robots)
            wait = False
            if not (last in (None, 'ore') and stock.ore - robots.ore >= blueprint.geode.ore and stock.obsidian - robots.obsidian >= blueprint.geode.obsidian):
                if stock.obsidian >= blueprint.geode.obsidian and stock.ore >= blueprint.geode.ore:
                    states.append((resources_add(robots, (0, 0, 0, 1)), 
                                   resources_sub(new_stock, blueprint.geode), 
                                   nb_minutes - 1,
                                   'geode'))
                else:
                    wait = robots.obsidian > 0
            if robots.ore < max_robots.ore and not (last in (None, 'ore') and stock.ore - robots.ore >= blueprint.ore.ore):
                if stock.ore >= blueprint.ore.ore:
                    states.append((resources_add(robots, (1, 0, 0, 0)), 
                                resources_sub(new_stock, blueprint.ore), 
                                nb_minutes - 1,
                                'ore'))
                else:
                    wait = True
            if robots.clay < max_robots.clay and not (last in (None, 'clay') and stock.ore - robots.ore >= blueprint.clay.ore): # and robots.clay * nb_minutes + stock[1] < max_robots[1] * nb_minutes:
                if stock.ore >= blueprint.clay.ore:
                    states.append((resources_add(robots, (0, 1, 0, 0)), 
                                resources_sub(new_stock, blueprint.clay), 
                                nb_minutes - 1,
                                'clay'))
                else:
                    wait = True
            if robots.obsidian < max_robots.obsidian and not (last in (None, 'obsidian') and stock.ore - robots.ore >= blueprint.obsidian.ore and stock.clay - robots.clay >= blueprint.obsidian.clay):
                if stock.ore >= blueprint.obsidian.ore and stock.clay >= blueprint.obsidian.clay: #and robots[2] * nb_minutes + stock[2] < max_robots[2] * nb_minutes:
                    states.append((resources_add(robots, (0, 0, 1, 0)), 
                                    resources_sub(new_stock, blueprint.obsidian), 
                                    nb_minutes - 1,
                                    'obsidian'))
                else:
                    wait = wait or robots.clay > 0
            if wait:
                states.append((robots, new_stock, nb_minutes - 1, None))
    return max_geodes


def part1(filepath: str) -> int:
    blueprints = load_blueprints(filepath)
    return sum((i + 1) * eval_blueprint(p, 24) for i, p in enumerate(blueprints))


def part2(filepath: str) -> int:
    blueprints = load_blueprints(filepath)
    return math.prod((eval_blueprint(p, 32) for p in blueprints[:3]))
    

if __name__ == "__main__":
    init_T(32)
    print(part1("inputs/day19.in"))
    print(part2("inputs/day19.in"))
