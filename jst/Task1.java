import java.io.IOException;
import java.io.InputStream;

public class Task1 {
    public static void main(String[] args) {
//        String[] input = getInput();
        String[] input = getTestInput();


    }

    private static String[] getTestInput() {
        String input = "";
        return input.split("\n");
    }

    private static String[] getInput() {
        try (InputStream resourceAsStream = Task1.class.getResourceAsStream("input.txt");){
            String input = new String(resourceAsStream.readAllBytes());
            return input.split("\r\n");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
