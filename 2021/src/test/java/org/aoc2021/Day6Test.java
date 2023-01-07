package org.aoc2021;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Day6Test {

    private final Day6 day6;

    public Day6Test() {
        day6 = new Day6();
    }
    @Test
    void part1() {
        assertEquals(5934, day6.part1());
    }

    @Test
    void part2() {
        assertEquals(26984457539L, day6.part2());
    }
}