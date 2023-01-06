package org.aoc2021;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Day1Test {

    private final Day1 day1;

    public Day1Test() {
        day1 = new Day1("inputs/day1.in");
    }
    @Test
    void part1() {
        assertEquals(7, day1.part1());
    }

    @Test
    void part2() {
        assertEquals(5, day1.part2());
    }
}