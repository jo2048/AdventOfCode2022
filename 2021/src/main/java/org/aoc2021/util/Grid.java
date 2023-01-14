package org.aoc2021.util;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Grid {

    public final int width;
    public final int height;
    private final int[][] array;

    public Grid(int width, int height) {
        this.width = width;
        this.height = height;
        array = new int[height][width];
    }

    public void setValue(Point p, int value) {
        array[p.y()][p.x()] = value;
    }

    public int getValue(Point p) {
        return array[p.y()][p.x()];
    }

    public boolean withinBounds(Point p) {
        return p.x() >= 0 && p.x() < width && p.y() >= 0 && p.y() < height;
    }

    public List<Point> getNeighbors(Point p) {
        return getNeighbors(p, false);
    }

    public List<Point> getNeighbors(Point p, boolean includeDiagonal) {
        return p.getNeighbors(includeDiagonal).stream().filter(this::withinBounds).collect(Collectors.toList());
    }

    public void incrementCell(Point p, int x) {
        array[p.y()][p.x()] += x;
    }

    public void incrementAllCells(int x) {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++)
                array[i][j] += x;
        }
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (int[] row : array)
            s.append(Arrays.toString(row)).append("\n");
        return s.toString();
    }
}
