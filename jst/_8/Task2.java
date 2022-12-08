package _8;

import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public class Task2 {
    public static void main(String[] args) {
        String input = getInput();

        String[] treeRows = input.split("\n");
        Map<Integer, String> threeRowsInverted = new HashMap<>();

        int maxScenicScore = 0;
        for (int i = 1; i < treeRows.length - 1; i++) {
            for (int j = 1; j < treeRows.length - 1; j++) {
                String horizontalTreeLine = treeRows[i];

                if (!threeRowsInverted.containsKey(j)) {
                    threeRowsInverted.put(j, getVerticalString(treeRows, j));
                }

                int scenicScoreHorizontal = isVisible(j, horizontalTreeLine);
                int scenicScoreVertical = isVisible(i, threeRowsInverted.get(j));

                int currentScenicScore = scenicScoreHorizontal * scenicScoreVertical;
                if (currentScenicScore > maxScenicScore) {
                    maxScenicScore = currentScenicScore;
                }
            }
        }
        System.out.println("maxScenicScore: " + maxScenicScore);
    }

    private static String getVerticalString(String[] treeRows, int j) {
        StringBuilder verticalString = new StringBuilder();
        for (String treeRow : treeRows) {
            verticalString.append(treeRow.charAt(j));
        }
        return verticalString.toString();
    }

    public static int isVisible(int indexInStringOfCurrentTree, String treeLine) {

        int heightOfCurrentTree = Character.getNumericValue(treeLine.charAt(indexInStringOfCurrentTree));

        int visibilityOne = 0;
        int visibilitySecond = 0;

        for (int i = indexInStringOfCurrentTree - 1; i >= 0; i--) {
            int heightOfPreviousTree = Character.getNumericValue(treeLine.charAt(i));
            visibilityOne++;
            if (heightOfPreviousTree >= heightOfCurrentTree) {
                break;
            }
        }
        for (int i = indexInStringOfCurrentTree + 1; i < treeLine.length(); i++) {

            int heightOfFollowingTree = Character.getNumericValue(treeLine.charAt(i));
            visibilitySecond++;
            if (heightOfFollowingTree >= heightOfCurrentTree) {
                break;
            }
        }

        return visibilityOne * visibilitySecond;
    }

    private static String getInput() {
        try (InputStream resourceAsStream = Task2.class.getResourceAsStream("input.txt")) {
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
