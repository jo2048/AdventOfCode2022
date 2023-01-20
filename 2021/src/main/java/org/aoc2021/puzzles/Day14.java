package org.aoc2021.puzzles;

import org.aoc2021.util.Counter;
import org.aoc2021.util.Util;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day14 implements Puzzle {

    private record Pair<T>(T e1, T e2) {}

    private final String template;
    private final HashMap<Pair<Character>, Pair<Pair<Character>>> rules;

    public Day14() {
        this("inputs/day14.in");
    }

    public Day14(String filepath) {
        List<String> lines = Util.readFile(filepath);
        template = lines.get(0);
        rules = new HashMap<>(lines.size());

        for (int i = 2; i < lines.size(); i++)
            parseRule(lines.get(i));
    }

    private void parseRule(String line) {
        String[] arr = line.split(" -> ");
        Pair<Character> output1 = new Pair<>(arr[0].charAt(0), arr[1].charAt(0));
        Pair<Character> output2 = new Pair<>(arr[1].charAt(0), arr[0].charAt(1));
        rules.put(new Pair<>(arr[0].charAt(0), arr[0].charAt(1)), new Pair<>(output1, output2));
    }

    private Counter<Pair<Character>> parseTemplate(String s) {
        Counter<Pair<Character>> counter = new Counter<>();
        for (int i = 0; i < s.length() - 1; i++)
            counter.add(new Pair<>(s.charAt(i), s.charAt(i + 1)));
        return counter;
    }

    private long compute(int nbSteps) {
        Counter<Character> characterCounter = new Counter<>();
        for (char c: template.toCharArray())
            characterCounter.add(c);

        Counter<Pair<Character>> counter = parseTemplate(template);
        for (int i = 0; i < nbSteps; i++) {
            Counter<Pair<Character>> result = new Counter<>();
            for (Map.Entry<Pair<Character>, Long> entry: counter.entrySet()) {
                if (rules.containsKey(entry.getKey())) {
                    Pair<Pair<Character>> o = rules.get(entry.getKey());
                    result.add(o.e1, entry.getValue());
                    result.add(o.e2, entry.getValue());
                    characterCounter.add(o.e2().e1, entry.getValue());
                }
            }
            counter = result;
        }
        return Collections.max(characterCounter.values()) - Collections.min(characterCounter.values());
    }

    @Override
    public String part1() {
        return String.valueOf(compute(10));
    }

    @Override
    public String part2() {
        return String.valueOf(compute(40));
    }
}
