package org.aoc2021.puzzles;

import org.aoc2021.util.Grid;
import org.aoc2021.util.Point;
import org.aoc2021.util.Util;

import java.util.*;

public class Day15 implements Puzzle {

    private final Grid grid;

    public Day15() {
        this("inputs/day15.in");
    }

    public Day15(String filepath) {
        grid = new Grid(Util.readFile(filepath));
    }

    @Override
    public String part1() {
        HashMap<Point, Integer> distances = new HashMap<>();
        distances.put(new Point(0, 0), 0);

        Set<Point> visited = Set.of(new Point(0, 0));
        PriorityQueue<Point> pq = new PriorityQueue<>(grid.height * grid.width / 2, Comparator.comparingInt(distances::get));
        pq.add(new Point(0, 0));

        while (pq.size() > 0) {
            Point p = pq.poll();
            int dist = distances.get(p);
            for (Point n: grid.getNeighbors(p)) {
                if (!visited.contains(n)) {
                    int newDistance = dist + grid.getValue(p);
                    if (!distances.containsKey(n) || newDistance < distances.get(n)) {
                        distances.put(n, newDistance);
                        pq.add(n);
                    }
                }
            }
        }

        return String.valueOf(distances.get(new Point(grid.width - 1, grid.height - 1)));
    }

    @Override
    public String part2() {
        return null;
    }
}
