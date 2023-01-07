package org.aoc2021;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public abstract class TestTemplate {

    private final Day day;
    private final String expectedPart1;
    private final String expectedPart2;

    protected TestTemplate(Day day, String expectedPart1, String expectedPart2) {
        this.day = day;
        this.expectedPart1 = expectedPart1;
        this.expectedPart2 = expectedPart2;
    }

    @Test
    void part1() {
        assertEquals(expectedPart1, day.part1());
    }

    @Test
    void part2() {
        assertEquals(expectedPart2, day.part2());
    }
}
