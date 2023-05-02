from util import readfile, Position
import re
from typing import Tuple, List


LINE_FORMAT = r'Sensor at x=(-?[\d]+), y=(-?[\d]+): closest beacon is at x=(-?[\d]+), y=(-?[\d]+)'


def parse_line(line: str) -> Tuple[int]:
    return (int(x) for x in list(map(int, re.findall(LINE_FORMAT, line)[0])))


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Sensor(Position):
    def __init__(self, x: int, y: int, beacon_x: int, beacon_y: int):
        Position.__init__(self, x, y)
        self.radius = manhattan_distance(x, y, beacon_x, beacon_y)

    def within_range(self, p: Position) -> bool:
        return manhattan_distance(self.x, self.y, p.x, p.y) <= self.radius

    def get_frontiers(self) -> Tuple[int]:
        d = self.radius + 1
        asc_1 = self.y - (self.x - d)
        asc_2 = self.y - (self.x + d)
        desc_1 = self.y + (self.x - d)
        desc_2 = self.y + (self.x + d)
        return asc_1, asc_2, desc_1, desc_2


################################ PART 1 ################################ 
def add_range(marked_intervals: List[tuple], interval: tuple):
    new_x1, new_x2 = interval
    i = 0
    join_left, join_right = False, False

    while i < len(marked_intervals) and new_x1 > marked_intervals[i][0]:
        i += 1

    j = i
    while j < len(marked_intervals) and new_x2 > marked_intervals[j][1]:
        j += 1    

    while j > i:
        marked_intervals.pop(j-1)
        j -= 1
        
    if i < len(marked_intervals) and new_x2 >= marked_intervals[i][0] - 1:
        join_right = True

    if i > 0 and new_x1 <= marked_intervals[i-1][1] + 1:
        join_left = True
    
    if join_left and join_right:
        left = marked_intervals.pop(i - 1)[0]
        right = marked_intervals.pop(i - 1)[1]
        marked_intervals.insert(i - 1, (left, right))
    elif join_left:
        left, maybe_right = marked_intervals.pop(i - 1)
        marked_intervals.insert(i - 1, (left, max(new_x2, maybe_right)))
    elif join_right:
        right = marked_intervals.pop(i)[1]
        marked_intervals.insert(i, (new_x1, right))
    else:
        marked_intervals.insert(i, (new_x1, new_x2))


def day15_1(filepath: str, line_y: int) -> int:
    lines = readfile(filepath)
    marked_intervals = []
    beacons_on_line = set()
    for line in lines:
        s_x, s_y, b_x, b_y = parse_line(line)
        if b_y == line_y:
            beacons_on_line.add(b_x)
        
        sensor = Sensor(s_x, s_y, b_x, b_y)

        if abs(sensor.y - line_y) <= sensor.radius:
            distance_to_line = abs(sensor.y - line_y)
            interval = sensor.x - (sensor.radius - distance_to_line), sensor.x + (sensor.radius - distance_to_line)
            add_range(marked_intervals, interval)

    covered = sum((x2 - x1) + 1 for x1, x2 in marked_intervals)
    return covered - len(beacons_on_line)


################################ PART 2 ################################ 
def is_valid_position(p: Position, sensors: List[Sensor], coord_limit: int):
    if not (0 < p.x < coord_limit and 0 < p.y < coord_limit):
        return False
    return all(not s.within_range(p) for s in sensors)


def intersection(frontier_asc, frontier_desc):
    return Position((frontier_desc - frontier_asc) // 2, (frontier_desc + frontier_asc) // 2)


def find_valid_position(sensors, limit) -> Position:
    for i in range(len(sensors)):
        s1 = sensors[i]
        s1_asc_1, s1_asc_2, s1_desc_1, s1_desc_2 = s1.get_frontiers()      
        for j in range(i + 1, len(sensors)):
            s2 = sensors[j] 
            s2_asc_1, s2_asc_2, s2_desc_1, s2_desc_2 = s2.get_frontiers()
            for p in (
                intersection(s1_asc_1, s2_desc_1),
                intersection(s1_asc_1, s2_desc_2),
                intersection(s1_asc_2, s2_desc_1),
                intersection(s1_asc_2, s2_desc_2),
                intersection(s2_asc_1, s1_desc_1),
                intersection(s2_asc_1, s1_desc_2),
                intersection(s2_asc_2, s1_desc_1),
                intersection(s2_asc_2, s1_desc_2)):
                if is_valid_position(p, sensors, limit):
                    return p


def day15_2(filepath: str, limit: int) -> int:
    lines = readfile(filepath)
    sensors = []
    for line in lines:
        s_x, s_y, b_x, b_y = parse_line(line)
        sensors.append(Sensor(s_x, s_y, b_x, b_y))

    p = find_valid_position(sensors, limit)
    return p.x * limit + p.y


if __name__ == "__main__":
    print(day15_1("inputs/day15.in", 2_000_000))
    print(day15_2("inputs/day15.in", 4_000_000))
