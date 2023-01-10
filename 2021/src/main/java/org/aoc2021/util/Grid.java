package org.aoc2021.util;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Grid {

    public final int width;
    public final int height;
    private short[][] array;

    public Grid(int width, int height) {
        this.width = width;
        this.height = height;
        array = new short[height][width];
    }

    public void setValue(Point p, short value) {
        array[p.y()][p.x()] = value;
    }

    public short getValue(Point p) {
        return array[p.y()][p.x()];
    }

    public boolean withinBounds(Point p) {
        return p.x() >= 0 && p.x() < width && p.y() >= 0 && p.y() < height;
    }

    public List<Point> getNeighbors(Point p) {
        return Arrays.stream(p.getNeighbors()).filter(this::withinBounds).collect(Collectors.toList());
    }

    @Override
    public String toString() {
        return Arrays.deepToString(array);
    }
}
