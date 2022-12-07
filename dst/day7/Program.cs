using System;
using System.Text;

namespace aoc2022
{
    class File
    {
        public string Name;
        public int Size;

        public File(string name, int size)
        {
            Name = name;
            Size = size;
        }
    }

    class Folder
    {
        public Folder? Parent;
        public string Name;
        public List<File> Files;
        public List<Folder> ChildFolders;
        public int Size;

        public Folder(string name, Folder parent)
        {
            Parent = parent;
            Name = name;
            Files = new();
            ChildFolders = new();
        }

        public void AddFile(string name, int size)
        {
            if (Files.Find(x => x.Name == name) == null)
            {
                Files.Add(new File(name, size));
            }
        }

        public void AddChildFolder(string name)
        {
            if (ChildFolders.Find(x => x.Name == name) == null)
            {
                Folder childFolder = new(name, this);
                ChildFolders.Add(childFolder);
            }
        }

        public Folder getChildFolder(string name)
        {
            return ChildFolders.Find(x => x.Name == name) ?? throw new KeyNotFoundException();
        }

        public Folder? getParentFolder()
        {
            return Parent;
        }
    }

    class day7
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "input.txt";
            // string filepath = "dani_sample.txt";

            // Initialize
            Folder root = new Folder("root", null);
            Folder currentFolder = root;

            // Parse Directory
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    switch (line[0])
                    {
                        case '$': currentFolder = command(currentFolder, line); break;
                        default: readitem(currentFolder, line); break;
                    }
                }
            }


            // printDirectory(root);
            // Compute total
            int total = computeFolderSizes(root);
            Console.WriteLine("Total Size: {0}", total);

            // Compute limit
            int limit = 100000;
            int sum = 0;
            computeLimitedSum(root, limit, ref sum);
            Console.WriteLine("Limited Sum: {0}", sum);

            // Part Two
            int requiredSize = 30000000;
            int diskSize = 70000000;
            int minDirectorySize = requiredSize - (diskSize - total);
            Console.WriteLine("Min Directory Size: {0}", minDirectorySize);

            int smallestDir = diskSize;
            findSmallestDir(root, minDirectorySize, ref smallestDir);
            Console.WriteLine("Smallest Dir Size: {0}", smallestDir);


        }

        public static Folder command(Folder currentFolder, string line)
        {
            if (line.Substring(2, 2) == "ls") { return currentFolder; };

            if (line[5] == '/')
            {
                return currentFolder;
            }
            else if (line[5] == '.')
            {
                return currentFolder.getParentFolder();
            }
            else
            {
                return currentFolder.getChildFolder(line.Substring(5));
            }
        }

        public static void readitem(Folder currentFolder, string line)
        {
            if (line.Substring(0, 3) == "dir")
            {
                currentFolder.AddChildFolder(line.Substring(4));
            }
            else
            {
                string[] splitString = line.Split();
                int size = int.Parse(splitString[0]);
                string name = splitString[1];
                currentFolder.AddFile(name, size);
            }
        }

        public static void printDirectory(Folder folder)
        {
            Console.WriteLine("{0}", folder.Name);

            foreach (Folder item in folder.ChildFolders)
            {
                printDirectory(item);
            }
        }

        public static int computeFolderSizes(Folder folder)
        {
            int subfoldersum = 0;
            foreach (Folder item in folder.ChildFolders)
            {
                subfoldersum += computeFolderSizes(item);
            }
            int filesum = folder.Files.Select(x => x.Size).Sum();
            folder.Size = filesum + subfoldersum;

            // Debug
            Console.WriteLine("Folder {0}: {1}", folder.Name, folder.Size);
            Console.WriteLine("- Filesum: {0}", filesum);
            Console.WriteLine("- Subfoldersum: {0}", subfoldersum);
            folder.ChildFolders.ForEach(x => Console.WriteLine("-- Folder: {0}, {1}", x.Name, x.Size));
            folder.Files.ForEach(x => Console.WriteLine("-- File: {0}, {1}", x.Name, x.Size));


            return filesum + subfoldersum;
        }

        public static void computeLimitedSum(Folder folder, int limit, ref int sum)
        {
            foreach (Folder item in folder.ChildFolders)
            {
                computeLimitedSum(item, limit, ref sum);
            }

            if (folder.Size < limit)
            {
                sum += folder.Size;
            }
        }

        public static void findSmallestDir(Folder folder, int minSize, ref int smallestDir)
        {
            foreach (Folder item in folder.ChildFolders)
            {
                findSmallestDir(item, minSize, ref smallestDir);
            }

            if (folder.Size > minSize && folder.Size < smallestDir)
            {
                smallestDir = folder.Size;
            }
        }
    }
}
