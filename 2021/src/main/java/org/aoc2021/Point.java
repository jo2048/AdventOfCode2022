package org.aoc2021;

public record Point(int x, int y) {

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return x == point.x && y == point.y;
    }

    public static Point loadFromString(String s) {
        String[] arr = s.split(",");
        return new Point(Integer.parseInt(arr[0]), Integer.parseInt(arr[1]));
    }
}
