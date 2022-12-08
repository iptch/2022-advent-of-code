package _3;

import java.io.IOException;
import java.io.InputStream;
import java.util.Set;
import java.util.stream.Collectors;

import static com.google.common.collect.Sets.intersection;

public class Task1_guavafied {

    public static void main(String[] args) {
        String input = getInput();
        String[] lines = input.split("\r\n");

        int result = 0;

        for (String line : lines) {
            String firstHalf = line.substring(0, line.length() / 2);
            String secondHalf = line.substring(line.length() / 2);

            Integer character = intersection(chars(firstHalf), chars(secondHalf)).iterator().next();

            int value = Character.isLowerCase(character) ? (character - ('a') + 1) : (character - 'A' + 27);
            result += value;
        }

        System.out.println(result);
    }

    private static Set<Integer> chars(String firstHalf) {
        return firstHalf.chars().boxed().collect(Collectors.toSet());
    }
    private static String getInput() {
        try (InputStream resourceAsStream = Task1_guavafied.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
