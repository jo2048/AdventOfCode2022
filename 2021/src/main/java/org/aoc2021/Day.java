package org.aoc2021;

public interface Day {

    String part1();
    String part2();
    default String getResult() {
        return getClass().getName() +
                "\n" +
                part1() +
                "\n" +
                part2();
    }
}
