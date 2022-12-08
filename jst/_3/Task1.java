package _3;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class Task1 {

    public static void main(String[] args) {

        List<String> listOfLowercaseCharacters = List.of("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
        Set<String> setOfLowercaseCharacters = Set.copyOf(listOfLowercaseCharacters);

        String input = getInput();

        String[] splitInput = input.split("\r\n");
        ArrayList<String> duplicates = new ArrayList<>();

        Integer sum = 0;
        for (String item : splitInput) {

            String theStart = item.substring(0, item.length() / 2);
            String theEnd = item.substring(item.length() / 2);

            for (int i = 0; i < theStart.length(); i++) {

                String currentChar = String.valueOf(theStart.charAt(i));
                if (theEnd.contains(currentChar)) {
                    duplicates.add(currentChar);
                    break;
                }
            }
        }

        for (String duplicate : duplicates) {
            sum += setOfLowercaseCharacters.contains(duplicate)
                    ? listOfLowercaseCharacters.indexOf(duplicate) + 1
                    : listOfLowercaseCharacters.indexOf(duplicate.toLowerCase()) + 1 + 26;
        }

        System.out.println(sum);
    }
    private static String getInput() {
        try (InputStream resourceAsStream = Task1.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
