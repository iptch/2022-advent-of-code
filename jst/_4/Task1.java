package _4;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Set;
import java.util.stream.Collectors;


public class Task1 {
    public static void main(String[] args) {
        String input = getInput();

        Integer sum = 0;

        String[] pairs = input.split("\n");

        for (int i = 0; i < pairs.length; i++) {

            String[] elvesPair = pairs[i].split(",");

            String[] firstElvesTodo = elvesPair[0].split("-");
            String[] secondElvesTodo = elvesPair[1].split("-");

            ArrayList<Integer> firstElvesRooms = new ArrayList<>();
            ArrayList<Integer> secondElvesRooms = new ArrayList<>();

            for (int j = Integer.parseInt(firstElvesTodo[0]); j <= Integer.parseInt(firstElvesTodo[1]); j++) {
                firstElvesRooms.add(j);
            }

            for (int j = Integer.parseInt(secondElvesTodo[0]); j <= Integer.parseInt(secondElvesTodo[1]); j++) {
                secondElvesRooms.add(j);
            }

            Set<Integer> result = firstElvesRooms.stream()
                    .distinct()
                    .filter(secondElvesRooms::contains)
                    .collect(Collectors.toSet());

            if (result.size() >= firstElvesRooms.size() ||  result.size() >= secondElvesRooms.size()) {
                sum += 1;
            }

        }
        System.out.println(sum);
        //582
    }
    private static String getInput() {
        try (InputStream resourceAsStream = Task1.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
