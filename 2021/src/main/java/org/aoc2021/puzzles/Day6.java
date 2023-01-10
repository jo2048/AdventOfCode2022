package org.aoc2021.puzzles;

import org.aoc2021.util.Point;
import org.aoc2021.util.Util;

import java.util.HashMap;

public class Day6 implements Puzzle {

    private final int[] fishes;
    private final HashMap<Point, Long> memo;

    public Day6() {
        this("inputs/day6.in");
    }

    public Day6(String filepath) {
        String[] arr = Util.readFile(filepath).get(0).split(",");
        fishes = new int[arr.length];
        for (int i = 0; i < arr.length; i++)
            fishes[i] = Integer.parseInt(arr[i]);

        memo = new HashMap<>();
    }

    public long nbFishes(int timer, int x) {
        if (x == 1)
            return 1;
        Long val = memo.get(new Point(timer, x));
        if (val == null) {
            if (timer == 1)
                val = nbFishes(9, x - 1) + nbFishes(7, x - 1);
            else
                val = nbFishes(timer - 1, x - 1);
            memo.put(new Point(timer, x), val);
        }
        return val;
    }

    public long totalFishesAfter(int days) {
        long total = 0;
        for (int fish : fishes)
            total += nbFishes(fish, days);
        return total;
    }

    public String part1() {
        return String.valueOf(totalFishesAfter(80));
    }

    public String part2() {
        return String.valueOf(totalFishesAfter(256));
    }
}
