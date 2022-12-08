package _2;

import java.io.IOException;
import java.io.InputStream;

class Task2 {
    public static void main(String[] args) {
        String input = getInput();
        int sum = 0;

        for (int i = 0; i < input.length(); i++) {

            if (String.valueOf(input.charAt(i)).equals("A") || String.valueOf(input.charAt(i)).equals("B") || String.valueOf(input.charAt(i)).equals("C")) {

                if (String.valueOf(input.charAt(i)).equals("A") && String.valueOf(input.charAt(i + 2)).equals("X")) {
                    sum += 3;
                }

                if (String.valueOf(input.charAt(i)).equals("A") && String.valueOf(input.charAt(i + 2)).equals("Y")) {
                    sum += 4;
                }

                if (String.valueOf(input.charAt(i)).equals("A") && String.valueOf(input.charAt(i + 2)).equals("Z")) {
                    sum += 8;
                }


                if (String.valueOf(input.charAt(i)).equals("B") && String.valueOf(input.charAt(i + 2)).equals("X")) {
                    sum += 1;
                }

                if (String.valueOf(input.charAt(i)).equals("B") && String.valueOf(input.charAt(i + 2)).equals("Y")) {
                    sum += 5;
                }

                if (String.valueOf(input.charAt(i)).equals("B") && String.valueOf(input.charAt(i + 2)).equals("Z")) {
                    sum += 9;
                }


                if (String.valueOf(input.charAt(i)).equals("C") && String.valueOf(input.charAt(i + 2)).equals("X")) {
                    sum += 2;
                }

                if (String.valueOf(input.charAt(i)).equals("C") && String.valueOf(input.charAt(i + 2)).equals("Y")) {
                    sum += 6;
                }

                if (String.valueOf(input.charAt(i)).equals("C") && String.valueOf(input.charAt(i + 2)).equals("Z")) {
                    sum += 7;
                }
            }
        }
        System.out.println(sum);
    }

    private static String getInput() {
        try (InputStream resourceAsStream = Task2.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}