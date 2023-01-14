package org.aoc2021.puzzles;

import org.aoc2021.util.Util;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Day8 implements Puzzle {

    private static class Line {
        final String[] input;
        final String[] output;

        Line(String s) {
            String[] arr = s.split(" \\| ");
            input = arr[0].split(" ");
            output = arr[1].split(" ");
        }
    }

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

    private Set<Character> stringToCharSet(String s) {
        return s.chars().mapToObj(e->(char)e).collect(Collectors.toSet());
    }

    private Set<Character> setIntersection(Set<Character> set1, Set<Character> set2) {
        Set<Character> set = new HashSet<>(set1);
        set.retainAll(set2);
        return set;
    }

    /*
     * At the index 0, the set of Characters used to display a 2
     * At the index 1, the set of Characters used to display a 4
     */
    private List<Set<Character>> computeSets(String[] input) {
        Set<Character> set2 = new HashSet<>();
        Set<Character> set4 = new HashSet<>();
        for (String s: input) {
            if (s.length() == 2)
                set2 = stringToCharSet(s);
            else if (s.length() == 4)
                set4 = stringToCharSet(s);
        }
        return List.of(set2, set4);
    }

    private int determineValue(String s, List<Set<Character>> sets) {
        Set<Character> set2 = sets.get(0);
        Set<Character> set4 = sets.get(1);
        if (s.length() == 2)
            return 1;
        if (s.length() == 3)
            return 7;
        if (s.length() == 4)
            return 4;
        if (s.length() == 7)
            return 8;
        if (s.length() == 6) {
            if (setIntersection(stringToCharSet(s), set2).size() == 1)
                return 6;
            else if (setIntersection(stringToCharSet(s), set4).size() == 3)
                return 0;
            return 9;
        }
        // s.length = 5
        if (setIntersection(stringToCharSet(s), set2).size() == 2)
            return 3;
        else if (setIntersection(stringToCharSet(s), set4).size() == 2)
            return 2;
        return 5;
    }

    @Override
    public String part2() {
        int sum = 0;
        for (Line line: data) {
            List<Set<Character>> sets = computeSets(line.input);
            int tmp = 0;
            for (String s: line.output) {
                tmp = tmp * 10 + determineValue(s, sets);
            }
            sum += tmp;
        }
        return String.valueOf(sum);
    }
}
