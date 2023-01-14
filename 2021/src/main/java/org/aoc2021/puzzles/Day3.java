package org.aoc2021.puzzles;

import org.aoc2021.util.Util;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.function.BiFunction;

public class Day3 implements Puzzle {

    private final List<String> lines;

    public Day3() {
        this("inputs/day3.in");
    }

    public Day3(String filepath) {
        lines = Util.readFile(filepath);
    }

    private boolean[] inverseArray(boolean[] array) {
        boolean[] result = new boolean[array.length];
        for (int i = 0; i < array.length; i++)
            result[i] = !array[i];
        return result;
    }

    private boolean[] computeMostPresent() {
        int[] counts = new int[lines.get(0).length()];
        for (String line: lines) {
            for (int i = 0; i < counts.length; i++)
                if (line.charAt(i) == '1')
                    counts[i] += 1;
        }
        boolean[] result = new boolean[counts.length];
        for (int i = 0; i < counts.length; i++)
            result[i] = counts[i] > lines.size() / 2;
        return result;
    }

    private int intFromArray(boolean[] array) {
        int result = 0;
        for (boolean bit : array) {
            result = result * 2 + (bit ? 1 : 0);
        }
        return result;
    }

    private int intFromString(String s) {
        int result = 0;
        for (char c: s.toCharArray()) {
            result = result * 2 + (c == '1' ? 1 : 0);
        }
        return result;
    }

    @Override
    public String part1() {
        boolean[] mostPresent = computeMostPresent();
        return String.valueOf(intFromArray(mostPresent) * intFromArray(inverseArray(mostPresent)));
    }

    private String filterPart2(BiFunction<Integer, Integer, Boolean> comparator) {
        List<String> result = new ArrayList<>(lines);
        List<String> a = new LinkedList<>();
        List<String> b = new LinkedList<>();
        for (int i = 0; i < lines.get(0).length(); i++) {
            if (result.size() == 1)
                return result.get(0);
            for (String s: result) {
                if (s.charAt(i) == '1')
                    a.add(s);
                else
                    b.add(s);
            }
            if (comparator.apply(a.size(), b.size()))
                result = a;
            else
                result = b;
            a = new LinkedList<>();
            b = new LinkedList<>();
        }
        return result.get(0);
    }

    @Override
    public String part2() {
        String mostCommon = filterPart2((a, b) -> a >= b);
        String leastCommon = filterPart2((a, b) -> a < b);
        return String.valueOf(intFromString(mostCommon) * intFromString(leastCommon));
    }
}
