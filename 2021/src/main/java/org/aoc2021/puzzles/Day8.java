package org.aoc2021.puzzles;

import org.aoc2021.util.Util;

import java.util.List;
import java.util.stream.Collectors;

public class Day8 implements Puzzle {

    private final List<Line> data;

    public Day8() {
        this("inputs/day8.in");
    }

    public Day8(String filepath) {
        data = Util.readFile(filepath).stream().map(Line::new).collect(Collectors.toList());
    }

    @Override
    public String part1() {
        int total = 0;
        for (Line line: data) {
            for (String s: line.output)
                if (s.length() <= 4 || s.length() == 7)
                    total += 1;
        }
        return String.valueOf(total);
    }

    private int determineValue(String s) {
        return 0;
    }

    @Override
    public String part2() {
        return null;
    }

    private static class Line {
        final String[] input;
        final String[] output;

        Line(String s) {
            String[] arr = s.split(" \\| ");
            input = arr[0].split(" ");
            output = arr[1].split(" ");
        }
    }
}
