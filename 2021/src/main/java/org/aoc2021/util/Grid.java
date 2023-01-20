package org.aoc2021.util;

import java.util.Arrays;
import java.util.Collection;
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

    public Grid(Collection<Point> points) {
        int xMax = 0, yMax = 0;
        int xMin = Integer.MAX_VALUE, yMin = Integer.MAX_VALUE;
        for (Point p: points) {
            xMax = Math.max(xMax, p.x());
            yMax = Math.max(yMax, p.y());
            xMin = Math.min(xMin, p.x());
            yMin = Math.min(yMin, p.y());
        }

        width = xMax - xMin + 1;
        height = yMax - yMin + 1;
        array = new int[height][width];

        Point origin = new Point(-xMin, -yMin);
        for (Point p: points)
            setValue(p.delta(origin), 1);
    }

    public Grid(List<String> lines) {
        this(lines.get(0).length(), lines.size());
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            for (int j = 0; j < line.length(); j++)
                array[i][j] = Integer.parseInt(line.substring(j, j + 1));
        }
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

    public String betterDisplay() {
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++)
                s.append(array[i][j] == 1 ? "#" : " ");
            s.append("\n");
        }
        return s.toString();
    }
}
