package org.aoc2021.util;

import java.util.*;

public class Counter<T> {

    private final HashMap<T, Long> counter;

    public Counter() {
        counter = new HashMap<>();
    }

    public Set<Map.Entry<T, Long>> entrySet() {
        return counter.entrySet();
    }

    public Set<T> keySet() {
        return counter.keySet();
    }

    public Collection<Long> values() {
        return counter.values();
    }

    public void add(T t) {
        add(t, 1);
    }

    public void add(T t, long x) {
        counter.merge(t, x, Long::sum);
    }

    public long getCount(T t) {
        if (counter.containsKey(t))
            return counter.get(t);
        return 0;
    }
}
