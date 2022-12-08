package _3;

import java.io.IOException;
import java.io.InputStream;
import java.util.Set;
import java.util.stream.Collectors;

import static com.google.common.collect.Sets.intersection;

public class Task2_guavafied {

    public static void main(String[] args) {
        String input = getInput();
        String[] lines = input.split("\r\n");

        int result = 0;

        for (int i = 0; i < lines.length; i += 3) {
            Integer containedInAll = intersection(intersection(chars(lines[i]), chars(lines[i + 1])), chars(lines[i + 2])).iterator().next();
            result += getPriority(containedInAll);
        }

        System.out.println(result);
    }

    private static int getPriority(Integer containedInAll) {
        return Character.isLowerCase(containedInAll) ? (containedInAll - ('a') + 1) : (containedInAll - 'A' + 27);
    }

    private static Set<Integer> chars(String firstHalf) {
        return firstHalf.chars().boxed().collect(Collectors.toSet());
    }

    private static String getInput() {
        try (InputStream resourceAsStream = Task2_guavafied.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
