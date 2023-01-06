package org.aoc2021;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Day2Test {

    private final Day2 day2;

    public Day2Test() {
        day2 = new Day2();
    }
    @Test
    void part1() {
        assertEquals(150, day2.part1());
    }

    @Test
    void part2() {
        assertEquals(900, day2.part2());
    }
}