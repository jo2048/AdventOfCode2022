package org.aoc2021.puzzles;

import org.aoc2021.util.Util;

import java.util.HashMap;
import java.util.List;

public class Day14 implements Puzzle {

    private final String start;
    private final HashMap<String, String> rules;

    public Day14() {
        this("inputs/day14.in");
    }

    public Day14(String filepath) {
        List<String> lines = Util.readFile(filepath);
        start = lines.get(0);

        rules = new HashMap<>(lines.size());
        for (int i = 2; i < lines.size(); i++) {
            String[] arr = lines.get(i).split(" -> ");
            rules.put(arr[0], arr[1]);
        }
    }

    @Override
    public String part1() {
        return null;
    }

    @Override
    public String part2() {
        return null;
    }
}
