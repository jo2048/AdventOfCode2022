package org.aoc2021.puzzles;

import org.aoc2021.util.Grid;
import org.aoc2021.util.Point;
import org.aoc2021.util.Util;

import java.util.*;
import java.util.function.BiFunction;

public class Day13 implements Puzzle {

    private static class Instruction {
        final String orientation;
        final int value;

        Instruction(String line) {
            String s = line.split(" ")[2];
            orientation = s.split("=")[0];
            value = Integer.parseInt(s.split("=")[1]);
        }
    }

    private final Set<Point> initialPoints;
    private final List<Instruction> instructions;

    public Day13() {
        this("inputs/day13.in");
    }

    public Day13(String filepath) {
        List<String> lines = Util.readFile(filepath);
        List<Point> points = new LinkedList<>();
        int i = 0;
        while (!lines.get(i).equals("")) {
            points.add(Point.loadFromString(lines.get(i)));
            i++;
        }
        initialPoints = Set.copyOf(points);

        instructions = new ArrayList<>(lines.size() - i);
        while (i + 1 < lines.size()) {
            i++;
            instructions.add(new Instruction(lines.get(i)));
        }
    }

    private Set<Point> fold(Set<Point> points, Instruction instruction) {
        BiFunction<Point, Integer, Point> newPointFunction = (p, value) -> p.x() > value ? new Point(2 * value - p.x(), p.y()) : p;
        if (instruction.orientation.equals("y"))
            newPointFunction = (p, value) -> p.y() > value ? new Point(p.x(), 2 * value - p.y()) : p;

        Set<Point> result = new HashSet<>();
        for (Point p : points)
            result.add(newPointFunction.apply(p, instruction.value));
        return result;
    }

    @Override
    public String part1() {
        return String.valueOf(fold(initialPoints, instructions.get(0)).size());
    }

    @Override
    public String part2() {
        Set<Point> pointsAfterFolding = new HashSet<>(initialPoints);
        for (Instruction instruction: instructions)
            pointsAfterFolding = fold(pointsAfterFolding, instruction);

        return String.valueOf(new Grid(pointsAfterFolding).betterDisplay());
    }
}
