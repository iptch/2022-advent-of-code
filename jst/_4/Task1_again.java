package _4;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class Task1_again {
    public static void main(String[] args) {
        String input = getInput();

        Integer sum = 0;

        String[] pairs = input.split("\r\n");

        for (int i = 0; i < pairs.length; i++) {

            String[] elvesPair = pairs[i].split(",");

            String[] firstElvesTodo = elvesPair[0].split("-");
            String[] secondElvesTodo = elvesPair[1].split("-");

            List<Integer> firstElvesRooms = IntStream.range(Integer.parseInt(firstElvesTodo[0]), Integer.parseInt(firstElvesTodo[1])+1).boxed().collect(Collectors.toList());
            List<Integer> secondElvesRooms = IntStream.range(Integer.parseInt(secondElvesTodo[0]), Integer.parseInt(secondElvesTodo[1])+1).boxed().collect(Collectors.toList());

            if(firstElvesRooms.containsAll(secondElvesRooms) || secondElvesRooms.containsAll(firstElvesRooms)){
                sum += 1;
            }
        }
        System.out.println(sum);
    }

    private static String getInput() {
        try (InputStream resourceAsStream = Task1_again.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
