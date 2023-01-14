package org.aoc2021.puzzles;

import org.aoc2021.util.Grid;
import org.aoc2021.util.Point;
import org.aoc2021.util.Util;

import java.util.*;

public class Day4 implements Puzzle {

    private final int[] order;
    private final List<Grid> grids;

    public Day4() {
        this("inputs/day4.in");
    }

    public Day4(String filepath) {
        List<String> lines = Util.readFile(filepath);

        // Parse first line
        String[] orderStr = lines.get(0).split(",");
        order = new int[orderStr.length];
        for (int i = 0; i < orderStr.length; i++)
            order[i] = Integer.parseInt(orderStr[i]);

        grids = new ArrayList<>();
        for (int i = 2; i + 5 <= lines.size(); i += 6)
            grids.add(parseGrid(lines, i));
    }

    private Grid parseGrid(List<String> lines, int startLine) {
        Grid grid = new Grid(5, 5);
        for (int i = startLine; i < startLine + 5; i++) {
            String[] strArray = lines.get(i).split(" +");
            List<Integer> intList = new ArrayList<>(5);
            for (String s: strArray)
                if (!s.equals(""))
                    intList.add(Integer.parseInt(s));
            for (int j = 0; j < 5; j++)
                grid.setValue(new Point(j, i - startLine), intList.get(j));
        }
        return grid;
    }

    private boolean checkRow(Grid grid, int rowIndex) {
        for (int i = 0; i < grid.width; i++) {
            if (grid.getValue(new Point(i, rowIndex)) != -1)
                return false;
        }
        return true;
    }

    private boolean checkColumn(Grid grid, int columnIndex) {
        for (int i = 0; i < grid.height; i++) {
            if (grid.getValue(new Point(columnIndex, i)) != -1)
                return false;
        }
        return true;
    }

    /*
     * Mark a number in the grid and return true if a row or column is completely marked after the operation
     */
    private boolean markNumber(Grid grid, int number) {
        for (int i = 0; i < grid.width; i++) {
            for (int j = 0; j < grid.height; j++) {
                if (grid.getValue(new Point(i, j)) == number) {
                    grid.setValue(new Point(i, j), -1);
                    if (checkRow(grid, j) || checkColumn(grid, i))
                        return true;
                }
            }
        }
        return false;
    }

    private int countUnmarkedNumbers(Grid grid) {
        int sum = 0;
        for (int i = 0; i < grid.width; i++) {
            for (int j = 0; j < grid.height; j++) {
                if (grid.getValue(new Point(i, j)) > 0)
                    sum += grid.getValue(new Point(i, j));
            }
        }
        return sum;
    }

    @Override
    public String part1() {
        for (int x: order) {
            for (Grid grid: grids) {
                if (markNumber(grid, x)) {
                    return String.valueOf(countUnmarkedNumbers(grid) * x);
                }
            }
        }
        return "";
    }

    @Override
    public String part2() {
        HashSet<Integer> markedGrids = new HashSet<>();
        for (int x: order) {
            for (int i = 0; i < grids.size(); i++) {
                if (!markedGrids.contains(i)) {
                    Grid grid = grids.get(i);
                    if (markNumber(grid, x)) {
                        if (markedGrids.size() == grids.size() - 1)
                            return String.valueOf(x * countUnmarkedNumbers(grid));
                        markedGrids.add(i);
                    }
                }
            }
        }
        return "";
    }
}
