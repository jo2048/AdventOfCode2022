package org.aoc2021;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Day7 implements Day {

    private final List<Integer> values;

    public Day7() {
        this("inputs/day7.in");
    }

    public Day7(String filepath) {
        values = Arrays.stream(Util.readFile(filepath).get(0).split(","))
                    .map(Integer::parseInt)
                    .sorted()
                    .collect(Collectors.toList());
    }

    @Override
    public String part1() {
        int median;
        int size = values.size();
        if (size % 2 == 0)
            median = (values.get(size / 2 - 1) + values.get(size / 2)) / 2;
        else
            median = values.get(size / 2);
        return String.valueOf(values
                                .stream()
                                .map(v -> Math.abs(v - median))
                                .reduce(Integer::sum).get());
    }

    @Override
    public String part2() {
        int minCost = Integer.MAX_VALUE;
        for (int i = values.get(0); i <= values.get(values.size() - 1); i++) {
            int finalI = i;
            minCost = Math.min(minCost, values
                    .stream().map(v -> costPart2(v, finalI))
                    .reduce(Integer::sum).get());
        }
        return String.valueOf(minCost);
    }

    public int costPart2(int a, int b) {
        return ((Math.abs(a - b) + 1) * Math.abs(a - b)) / 2;
    }
}
