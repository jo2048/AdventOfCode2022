package org.aoc2021.util;

import java.util.List;

public record Point(int x, int y) {

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return x == point.x && y == point.y;
    }

    public Point[] getNeighbors() {
        return new Point[]{new Point(x + 1, y), new Point(x - 1, y), new Point(x, y - 1), new Point(x, y + 1)};
    }

    public static Point loadFromString(String s) {
        String[] arr = s.split(",");
        return new Point(Integer.parseInt(arr[0]), Integer.parseInt(arr[1]));
    }
}
