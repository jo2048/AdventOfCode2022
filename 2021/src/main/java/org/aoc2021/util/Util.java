package org.aoc2021.util;

import java.io.IOException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Util {

    public static List<String> readFile(String filepath) {
        URL resource = Util.class.getClassLoader().getResource(filepath);
        List<String> list;
        try {
            list = Files.readAllLines(Path.of(resource.getPath()));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return list;
    }

}
