package org.aoc2021.puzzles;

import org.aoc2021.puzzles.Puzzle;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public abstract class PuzzleTestTemplate {

    private final Puzzle puzzle;
    private final String expectedPart1;
    private final String expectedPart2;

    protected PuzzleTestTemplate(Puzzle puzzle, String expectedPart1, String expectedPart2) {
        this.puzzle = puzzle;
        this.expectedPart1 = expectedPart1;
        this.expectedPart2 = expectedPart2;
    }

    @Test
    void part1() {
        assertEquals(expectedPart1, puzzle.part1());
    }

    @Test
    void part2() {
        assertEquals(expectedPart2, puzzle.part2());
    }
}
