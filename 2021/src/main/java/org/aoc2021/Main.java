package org.aoc2021;

import org.aoc2021.puzzles.*;

public class Main {
    public static void main(String[] args) {
        Puzzle[] puzzles = {
                new Day1(), new Day2(), new Day3(), new Day4(), new Day5(),
                new Day6(), new Day7(), new Day8(), new Day9(), new Day11(),
                new Day13(), new Day14(), new Day15()};
        for (Puzzle puzzle : puzzles)
            System.out.println(puzzle.getResult());
    }
}