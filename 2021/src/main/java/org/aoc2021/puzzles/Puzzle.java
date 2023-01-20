package org.aoc2021.puzzles;

public interface Puzzle {

    String part1();
    String part2();
    default String getResult() {
        return getClass().getSimpleName() +
                "\n" +
                part1() +
                "\n" +
                part2() +
                "\n";
    }
}
