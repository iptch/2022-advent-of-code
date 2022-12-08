package _1;

import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

class Task1 {
    public static void main(String[] args) {
        String input = getInput();

        String[] splitInput = input.split("\r\n");
        List<String> elvesFood = List.of(splitInput);


        int maxCalories = 0;
        int[] irgendwas = new int[3];
        int sum = 0;
        for (String calorie : elvesFood) {
            if (!calorie.equals("")) {
                sum += Integer.parseInt(calorie);
            } else {
                if (sum >= irgendwas[0]) {
                    maxCalories = sum;
                    int index = Arrays.binarySearch(irgendwas, sum);
                    if (index == -2) {
                        irgendwas[0] = sum;
                    }
                    if (index == -3) {
                        irgendwas[0] = irgendwas[1];
                        irgendwas[1] = sum;
                    }
                    if (index == -4) {
                        irgendwas[0] = irgendwas[1];
                        irgendwas[1] = irgendwas[2];
                        irgendwas[2] = sum;
                    }
                }
                sum = 0;
            }
        }
        System.out.println(maxCalories);
        System.out.println(IntStream.of(irgendwas).sum());
    }

    private static String getInput() {
        try (InputStream resourceAsStream = Task1.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}