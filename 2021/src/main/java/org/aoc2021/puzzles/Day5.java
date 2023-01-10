package org.aoc2021.puzzles;

import org.aoc2021.util.Point;
import org.aoc2021.util.Util;

import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class Day5 implements Puzzle {

    private final List<Vent> vents;

    public Day5() {
        this("inputs/day5.in");
    }

    public Day5(String filepath) {
        vents = Util.readFile(filepath).stream().map(Vent::new).collect(Collectors.toList());
    }

    public int countDangerousPoints(boolean includeDiagonalVents) {
        HashMap<Point, Integer> map = new HashMap<>();
        for (Vent v: vents) {
            Point p1 = v.p1;
            Point p2 = v.p2;
            if (p1.x() == p2.x()) {
                for (int i = Math.min(p1.y(), p2.y()); i <= Math.max(p1.y(), p2.y()); i++)
                    map.merge(new Point(p1.x(), i), 1, Integer::sum);
            } else if (v.p1.y() == v.p2.y()) {
                for (int i = Math.min(p1.x(), p2.x()); i <= Math.max(p1.x(), p2.x()); i++)
                    map.merge(new Point(i, p1.y()), 1, Integer::sum);
            } else if (includeDiagonalVents && Math.abs(p1.x() - p2.x()) == Math.abs(p1.y() - p2.y())) {
                if (p1.x() > p2.x()) {
                    Point tmp = p1;
                    p1 = p2;
                    p2 = tmp;
                }
                int coefficient = 1;
                if (p1.x() - p2.x() == p2.y() - p1.y())
                    coefficient = -1;
                for (int i = 0; i <= p2.x() - p1.x(); i++) {
                    int x = p1.x() + i;
                    int y = p1.y() + i * coefficient;
                    map.merge(new Point(x, y), 1, Integer::sum);
                }
            }
        }
        return (int) map.entrySet().stream()
                .filter(entry -> entry.getValue() > 1)
                .count();
    }

    @Override
    public String part1() {
        return String.valueOf(countDangerousPoints(false));
    }

    @Override
    public String part2() {
        return String.valueOf(countDangerousPoints(true));
    }

    private static class Vent {
        private final Point p1;
        private final Point p2;

        Vent(String line) {
            String[] arr = line.split(" -> ");
            p1 = Point.loadFromString(arr[0]);
            p2 = Point.loadFromString(arr[1]);
        }
    }
}
