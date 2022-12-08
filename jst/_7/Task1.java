package _7;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Task1 {
    public static void main(String[] args) {

        String input = getInput();

        String[] lines = input.split("\r\n");

        String navigateInto = "\\$ cd (.+)";
        String file = "(\\d+) (.+)";
        String navigateToRoot = "$ cd /";
        String navigateBack = "\\$ cd ..";

        Directory rootDirectory = new Directory();
        Directory currentDirectory = rootDirectory;

        for (String line : lines) {
            if (navigateToRoot.equals(line)) {
                currentDirectory = rootDirectory;
            } else if (line.matches(navigateBack)) {
                currentDirectory = currentDirectory.parent;
            } else if (line.matches(navigateInto)) {
                String directory = getMatchingString(navigateInto, line, 1);
                currentDirectory = currentDirectory.addDirectory(directory);
            } else if (line.matches(file)) {
                String size = getMatchingString(file, line, 1);
                String name = getMatchingString(file, line, 2);
                currentDirectory.addFile(name, size);
            }
        }

        rootDirectory.computeSum();
        ArrayList<Directory> directories = new ArrayList<>();
        rootDirectory.greaterThan(directories);

        int totalSizeOfDirectories = directories.stream().mapToInt(d -> d.sum).sum();
        System.out.println("total size of directories " + totalSizeOfDirectories);
    }

    private static String getMatchingString(String navigateInto, String line, int groupIndex) {
        Matcher matcher = Pattern.compile(navigateInto).matcher(line);
        matcher.find();
        return matcher.group(groupIndex);
    }

    public static class Directory {
        public Directory() {
        }

        public Directory parent;
        public List<File> files = new ArrayList<>();
        public List<Directory> directories = new ArrayList<>();
        public String name;

        public int sum;

        public Directory(String name) {
            this.name = name;
        }

        public Directory addDirectory(String name) {
            boolean exists = directories.stream().anyMatch(d -> d.name.equals(name));
            if (!exists) {
                Directory directory = new Directory(name);
                directories.add(directory);
                directory.parent = this;
            }
            return directories.stream().filter(d -> d.name.equals(name)).findAny().get();
        }

        public void addFile(String name, String size) {
            files.add(new File(name, Integer.valueOf(size)));
        }

        public void computeSum() {
            directories.forEach(Directory::computeSum);
            int sumOfFiles = files.stream().mapToInt(file -> file.size).sum();
            this.sum = sumOfFiles + directories.stream().mapToInt(d -> d.sum).sum();
        }

        public void greaterThan(List<Directory> directories) {
            if (sum <= 100000) {
                directories.add(this);
            }
            this.directories.forEach(d -> d.greaterThan(directories));
        }
    }

    public static class File {
        public File(String name, Integer size) {
            this.name = name;
            this.size = size;
        }

        String name;
        Integer size;
    }

    private static String getInput() {
        try (InputStream resourceAsStream = Task1.class.getResourceAsStream("input.txt");){
            return new String(resourceAsStream.readAllBytes());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
