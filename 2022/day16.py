from util import readfile, dijkstra
from collections import defaultdict
import re


LINE_FORMAT = re.compile(r'Valve ([A-Z]{2}) has flow rate=([\d]+); tunnels? leads? to valves? (.*)')


def parse_graph(filepath: str):
    lines = readfile(filepath)
    edges = defaultdict(dict)
    flow_dict = dict()
    for line in lines:
        source, flow, destinations = LINE_FORMAT.findall(line)[0]
        flow_dict[source] = int(flow) 
        for destination in destinations.split(', '):
            edges[source][destination] = 1
            edges[destination][source] = 1

    return flow_dict, edges


def load_and_simplify_graph(filepath):
    flow_dict, edges = parse_graph(filepath)

    interesting_vertices = set(v for v in flow_dict if flow_dict[v] > 0)
    interesting_vertices.add('AA')

    simplified_edges = defaultdict(dict)

    for v in interesting_vertices:
        distance_from_v = dijkstra(v, flow_dict.keys(), edges)
        for v2 in distance_from_v:
            if v2 in interesting_vertices:
                simplified_edges[v][v2] = distance_from_v[v2]

    return flow_dict, interesting_vertices, simplified_edges


def maximize_flow(flow, edges, interesting_vertices, remaining_turns) -> dict:
    states = [('AA', 0, 0, interesting_vertices - set(('AA',)), remaining_turns)]
    max_flow = 0
    while len(states) > 0:
        node, total_flow, current_flow, closed_valves, remaining_turns = states.pop()
        max_flow = max(max_flow, total_flow + (current_flow + flow[node]) * remaining_turns)
        for v in closed_valves:
            cost = edges[node][v] 
            if cost + 1 < remaining_turns:
                states.append((v, total_flow + (current_flow + flow[node]) * (cost + 1), current_flow + flow[node], closed_valves - set((v,)), remaining_turns - 1 - cost))
    return max_flow


def part1(filepath: str, nb_minutes: int) -> int:
    flow_dict, interesting_vertices, edges = load_and_simplify_graph(filepath)
    return maximize_flow(flow_dict, edges, interesting_vertices, nb_minutes)


def maximize_flow_part2(flow, edges, interesting_vertices, remaining_turns) -> int:
    states = [('AA', 'AA', 0, 0, 0, 0, interesting_vertices - set(('AA',)), remaining_turns)]
    max_flow = 0
    while len(states) > 0:
        node_a, node_b, travel_time_a, travel_time_b, total_flow, current_flow, closed_valves, remaining_turns = states.pop()
        # print(node_a, node_b, travel_time_a, travel_time_b, total_flow, current_flow, closed_valves, remaining_turns)
        flow_a = flow[node_a] if travel_time_a == 0 else 0
        flow_b = flow[node_b] if travel_time_b == 0 else 0
        max_flow = max(max_flow, total_flow + (current_flow + flow_a + flow_b) * remaining_turns)
        if travel_time_a == 0:
            for v in closed_valves:
                cost = edges[node_a][v]
                if cost + 1 < remaining_turns:
                    travel_time = min(cost + 1, travel_time_b)
                    states.append((v, node_b, cost + 1 - travel_time, travel_time_b - travel_time, total_flow + (current_flow + flow[node_a]) * travel_time, current_flow + flow[node_a], closed_valves - set((v,)), remaining_turns - travel_time))
        elif travel_time_b == 0:
            # print('ici - ', travel_time_b)
            for v in closed_valves:
                cost = edges[node_b][v]
                if cost + 1 < remaining_turns:
                    travel_time = min(cost + 1, travel_time_a)
                    states.append((node_a, v, travel_time_a - travel_time, cost + 1 - travel_time, total_flow + (current_flow + flow[node_b]) * travel_time, current_flow + flow[node_b], closed_valves - set((v,)), remaining_turns - travel_time))

    return max_flow


def part2(filepath: str, nb_minutes: int) -> int:
    flow_dict, interesting_vertices, edges = load_and_simplify_graph(filepath)
    return maximize_flow_part2(flow_dict, edges, interesting_vertices, nb_minutes)


if __name__ == '__main__':
    print(part1("inputs/day16.in", 30))
    # import time
    # for i in range(1, 27):
    #     print(i, ' - ', part2("test/day16.in", i))
    # t  = time.time()
    # # print(part1("inputs/day16.in", 30)) #1720
    # print(part2("inputs/day16.in", 26))
    # t = time.time() - t
    # print(t)
    
    # print(day16_2("test/day16.in"))
