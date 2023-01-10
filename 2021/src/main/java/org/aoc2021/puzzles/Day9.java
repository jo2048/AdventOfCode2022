package org.aoc2021.puzzles;

import org.aoc2021.util.*;

import java.util.*;

public class Day9 implements Puzzle {

    private final Grid grid;

    public Day9() {
        this("inputs/day9.in");
    }

    public Day9(String filepath) {
        List<String> lines = Util.readFile(filepath);
        grid = new Grid(lines.get(0).length(), lines.size());
        for (int i = 0; i < lines.size(); i++) {
            for (int j = 0; j < lines.get(0).length(); j ++)
                grid.setValue(new Point(j, i), Short.parseShort(lines.get(i).substring(j, j + 1)));
        }
    }

    private List<Point> findLowPoints() {
        List<Point> lowPoints = new ArrayList<>();
        for (int i = 0; i < grid.width; i++) {
            for (int j = 0; j < grid.height; j++) {
                Point p = new Point(i, j);
                int v = grid.getValue(p);
                boolean lowPoint = true;
                for (Point n : grid.getNeighbors(p)) {
                    if (grid.getValue(n) <= v) {
                        lowPoint = false;
                        break;
                    }
                }
                if (lowPoint)
                    lowPoints.add(p);
            }
        }
        return lowPoints;
    }

    @Override
    public String part1() {
        int sum = 0;
        for (Point p : findLowPoints())
            sum += grid.getValue(p) + 1;
        return String.valueOf(sum);
    }

    private int computeBasinSize(Grid grid, Point start) {
        LinkedList<Point> fifo = new LinkedList<>();
        fifo.add(start);
        Set<Point> basin = new HashSet<>(fifo);
        while (fifo.size() > 0) {
            Point p = fifo.pop();
            basin.add(p);
            for (Point n : grid.getNeighbors(p)) {
                if (!basin.contains(n) && grid.getValue(n) < 9)
                    fifo.add(n);
            }
        }
        return basin.size();
    }

    @Override
    public String part2() {
        List<Integer> basins = new ArrayList<>();
        for (Point p : findLowPoints())
            basins.add(computeBasinSize(grid, p));
        basins.sort(Collections.reverseOrder());
        return String.valueOf(basins.get(0) * basins.get(1) * basins.get(2));
    }
}
