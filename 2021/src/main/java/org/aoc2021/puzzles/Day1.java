package org.aoc2021.puzzles;

import java.util.List;
import java.util.stream.Collectors;

import static org.aoc2021.util.Util.readFile;

public class Day1 implements Puzzle {

    private final List<Integer> values;

    public Day1() {
        this("inputs/day1.in");
    }

    public Day1(String filepath) {
        values = readFile(filepath).stream().map(Integer::parseInt).collect(Collectors.toList());
    }

    @Override
    public String part1() {
        int result = 0;
        int old_val = Integer.MAX_VALUE;
        for (int val: values) {
            if (val > old_val)
                result += 1;
            old_val = val;
        }
        return String.valueOf(result);
    }

    @Override
    public String part2() {
        int result = 0;
        int old_val = Integer.MAX_VALUE;
        for (int i = 0; i < values.size() - 2; i++) {
            int val = sumArrayElements(i);
            if (val > old_val)
                result += 1;
            old_val = val;
        }
        return String.valueOf(result);
    }

    private int sumArrayElements(int startIndex) {
        return values.get(startIndex) + values.get(startIndex + 1) + values.get(startIndex + 2);
    }
}
