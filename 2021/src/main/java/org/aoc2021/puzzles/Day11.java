package org.aoc2021.puzzles;

import org.aoc2021.util.Grid;
import org.aoc2021.util.Point;
import org.aoc2021.util.Util;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Day11 implements Puzzle {

    private final Grid grid;
    private int part1Result;
    private int part2Result;

    public Day11() {
        this("inputs/day11.in");
    }

    public Day11(String filepath) {
        List<String> lines = Util.readFile(filepath);
        grid = new Grid(lines.get(0).length(), lines.size());
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            for (int j = 0; j < line.length(); j++)
                grid.setValue(new Point(j, i), Short.parseShort(line.substring(j, j + 1)));
        }

        part1Result = -1;
        part2Result = -1;
    }

    private void computeResults() {
        int part1 = 0;
        int step = 0;
        while (part1Result == -1 || part2Result == -1) {
            step += 1;
            grid.incrementAllCells(1);
            Set<Point> markedPoints = new HashSet<>();
            boolean modified = true;
            while (modified) {
                modified = false;
                for (int i = 0; i < grid.width; i++) {
                    for (int j = 0; j < grid.height; j++) {
                        Point p = new Point(i, j);
                        if (!markedPoints.contains(p) && grid.getValue(p) > 9) {
                            markedPoints.add(p);
                            for (Point n : grid.getNeighbors(p, true))
                                grid.incrementCell(n, 1);
                            modified = true;
                        }
                    }
                }
            }
            for (int i = 0; i < grid.width; i++) {
                for (int j = 0; j < grid.height; j++) {
                    Point p = new Point(i, j);
                    if (grid.getValue(p) > 9)
                        grid.setValue(p, 0);
                }
            }
            part1 += markedPoints.size();

            if (part2Result == -1 && markedPoints.size() == grid.height * grid.width)
                part2Result = step;
            if (step == 100)
                part1Result = part1;
        }
    }

    @Override
    public String part1() {
        if (part1Result == -1)
            computeResults();
        return String.valueOf(part1Result);
    }

    @Override
    public String part2() {
        if (part2Result == -1)
            computeResults();
        return String.valueOf(part2Result);
    }
}
