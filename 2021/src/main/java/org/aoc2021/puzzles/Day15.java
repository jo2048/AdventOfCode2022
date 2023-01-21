package org.aoc2021.puzzles;

import org.aoc2021.util.Grid;
import org.aoc2021.util.Point;
import org.aoc2021.util.Util;

import java.util.*;

public class Day15 implements Puzzle {

    private record PriorityPoint(int priority, Point point) {};

    private final Grid grid;

    public Day15() {
        this("inputs/day15.in");
    }

    public Day15(String filepath) {
        grid = new Grid(Util.readFile(filepath));
    }

    public int getCost(Point p) {
        assert p.x() >= 0 && p.y() >= 0;
        if (grid.withinBounds(p))
            return grid.getValue(p);
        int deltaX = p.x() / grid.width;
        int deltaY = p.y() / grid.height;
        int cost = grid.getValue(new Point(p.x() % grid.width, p.y() % grid.height)) + deltaY + deltaX;
        return cost < 10 ? cost : cost % 9;
    }

    private int shortestPath(Point start, Point end) {
        HashMap<Point, Integer> distances = new HashMap<>();
        distances.put(start, 0);

        Set<Point> visited = new HashSet<>();
        PriorityQueue<PriorityPoint> pq = new PriorityQueue<>(end.y() * end.x() / 2, Comparator.comparingInt(PriorityPoint::priority));
        pq.add(new PriorityPoint(0, start));

        while (pq.size() > 0) {
            PriorityPoint pp = pq.poll();
            Point p = pp.point();
            visited.add(p);
            int dist = distances.get(p);
            for (Point n: p.getNeighbors()) {
                if (n.equals(end))
                    return dist + getCost(n);
                if (n.x() >= 0 && n.y() >= 0 && n.x() <= end.x() && n.y() <= end.y() && !visited.contains(n)) {
                    int newDistance = dist + getCost(n);
                    if (!distances.containsKey(n) || distances.get(n) > newDistance) {
                        distances.put(n, newDistance);
                        pq.add(new PriorityPoint(newDistance, n));
                    }
                }
            }
        }
        return distances.get(end);
    }

    @Override
    public String part1() {
        return String.valueOf(shortestPath(new Point(0, 0), new Point(grid.width - 1, grid.height - 1)));
    }

    @Override
    public String part2() {
        //2885
        return String.valueOf(shortestPath(new Point(0, 0), new Point(5 * grid.width - 1, 5 * grid.height - 1)));
    }
}
