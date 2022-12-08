package _8;

import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public class Task1 {
    public static void main(String[] args) {
        String input = getInput();

        String[] treeRows = input.split("\r\n");
        Map<Integer, String> threeRowsInverted = new HashMap<>();

        int numberOfOuterVisibleTrees = treeRows[0].length() * 2 + (2 * (treeRows.length - 2));
        int numberOfInnerVisibleTrees = 0;
        for (int i = 1; i < treeRows.length - 1; i++) {
            for (int j = 1; j < treeRows.length - 1; j++) {
                String horizontalTreeLine = treeRows[i];

                if (!threeRowsInverted.containsKey(j)) {
                    threeRowsInverted.put(j, getVerticalString(treeRows, j));
                }

                boolean isVisibleOnHorizontalLine = isVisible(j, horizontalTreeLine);
                boolean isVisibleOnVerticalLine = isVisible(i, threeRowsInverted.get(j));

                if (isVisibleOnHorizontalLine || isVisibleOnVerticalLine) {
                    numberOfInnerVisibleTrees += 1;
                }
            }
        }


        System.out.println("Number of visible trees " + (numberOfOuterVisibleTrees + numberOfInnerVisibleTrees));


    }

    private static String getVerticalString(String[] treeRows, int j) {
        StringBuilder verticalString = new StringBuilder();
        for (String treeRow : treeRows) {
            verticalString.append(treeRow.charAt(j));
        }
        return verticalString.toString();
    }

    public static boolean isVisible(int indexInStringOfCurrentTree, String treeLine) {

        int heightOfCurrentTree = Character.getNumericValue(treeLine.charAt(indexInStringOfCurrentTree));
        boolean isVisibleOne = true;
        boolean isVisibleTwo = true;

        for (int i = 0; i < treeLine.length(); i++) {
            int heightOfTreeAround = Character.getNumericValue(treeLine.charAt(i));
            if (i < indexInStringOfCurrentTree && heightOfTreeAround >= heightOfCurrentTree) {
                isVisibleOne = false;
            } else if (i > indexInStringOfCurrentTree && heightOfTreeAround >= heightOfCurrentTree) {
                isVisibleTwo = false;
            }
        }

        return isVisibleOne || isVisibleTwo;
    }


    private static String getInput() {
        try (InputStream resourceAsStream = Task1.class.getResourceAsStream("input.txt");){
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
