package org.aoc2021;

import java.util.List;

public class Day2 {

    private final List<String> lines;

    public Day2() {
        lines = Util.readFile("inputs/day2.in");
    }


    public int part1() {
        int x = 0;
        int y = 0;
        for (String line: lines) {
            Command cmd = new Command(line);
            switch (cmd.instruction) {
                case "down" -> y += cmd.val;
                case "up" -> y -= cmd.val;
                default -> x += cmd.val;
            }
        }
        return x * y;
    }

    public int part2() {
        int x = 0;
        int y = 0;
        int aim = 0;
        for (String line: lines) {
            Command cmd = new Command(line);
            switch (cmd.instruction) {
                case "down" -> aim += cmd.val;
                case "up" -> aim -= cmd.val;
                default -> {
                    x += cmd.val;
                    y += aim * cmd.val;
                }
            }
        }
        return x * y;
    }

    private static class Command {
        String instruction;
        int val;

        Command(String line) {
            String[] arr = line.split(" ");
            instruction = arr[0];
            val = Integer.parseInt(arr[1]);
        }
    }
}
