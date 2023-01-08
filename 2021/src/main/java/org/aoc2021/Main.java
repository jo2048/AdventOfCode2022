package org.aoc2021;

public class Main {
    public static void main(String[] args) {
        Day[] days = {new Day1(), new Day2(), new Day5(), new Day6(), new Day7()};
        for (Day day : days)
            System.out.println(day.getResult());
    }
}