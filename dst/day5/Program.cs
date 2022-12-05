using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day5
    {
        public static void Main(string[] args)
        {


            // string filepath = "sample_input.txt";
            // const int NUMBER_OF_STACKS = 3;
            // const int STACK_HEIGHT = 3;
            string filepath = "input.txt";
            const int NUMBER_OF_STACKS = 9;
            const int STACK_HEIGHT = 8;

            List<List<char>> stacks = new();
            List<List<int>> commands = new();

            InitializeStacks(NUMBER_OF_STACKS, stacks);
            ParseStacks(filepath, NUMBER_OF_STACKS, STACK_HEIGHT, stacks);
            ParseCommatacks(stacks, NUMBER_OF_STACKS); nds(filepath, STACK_HEIGHT, commands);
            commands.ForEach(item => executeCommand(stacks, item));
            PrintTopItems(stacks);

            stacks.Clear();
            InitializeStacks(NUMBER_OF_STACKS, stacks);
            ParseStacks(filepath, NUMBER_OF_STACKS, STACK_HEIGHT, stacks);
            commands.ForEach(item => executeCommandPartTwo(stacks, item));
            PrintTopItems(stacks);

        }

        private static void PrintTopItems(List<List<char>> stacks)
        {
            Console.Write("Top items: ");
            stacks.ForEach(item => Console.Write(item[0]));
            Console.Write("\n");
        }

        private static void executeCommand(List<List<char>> stacks, List<int> command)
        {
            for (int i = 0; i < command[0]; i++)
            {

                var currentCrate = stacks[command[1] - 1][0];
                stacks[command[1] - 1].RemoveAt(0);
                stacks[command[2] - 1].Insert(0, currentCrate);
            }
        }

        private static void executeCommandPartTwo(List<List<char>> stacks, List<int> command)
        {
            int cratesMoved = command[0];
            int fromStack = command[1] - 1;
            int toStack = command[2] - 1;

            stacks[toStack].InsertRange(0, stacks[fromStack].Take(cratesMoved));
            stacks[fromStack].RemoveRange(0, cratesMoved);
        }

        private static void ParseCommands(string filepath, int STACK_HEIGHT, List<List<int>> commands)
        {
            int lineNumber = 1;
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    if (lineNumber > STACK_HEIGHT + 2)
                    {
                        List<int> command = new();
                        string[] splitLine = line.Split().ToArray();
                        for (int i = 0; i < 3; i++)
                        {
                            command.Add(int.Parse(splitLine[((i + 1) * 2 - 1)]));
                        }
                        commands.Add(command);
                    }
                    lineNumber++;
                }
            }
        }

        private static void PrintCommands(List<List<int>> commmands)
        {
            foreach (List<int> item in commmands)
            {
                Console.Write("m {0} f {1} t {2} \n", item[0], item[1], item[2]);
            }
        }
        private static void ParseStacks(string filepath, int NUMBER_OF_CRATES, int STACK_HEIGHT, List<List<char>> crates)
        {
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                int stack_level = 0;
                while ((line = sr.ReadLine()) != "" && stack_level < STACK_HEIGHT)
                {
                    int j = 1;
                    for (int i = 0; i < NUMBER_OF_CRATES; i++)
                    {
                        char crate = line[j];
                        if (crate != ' ') { crates[i].Add(crate); };
                        j += 4;
                    }
                    stack_level++;
                }
            }
        }

        private static void InitializeStacks(int NUMBER_OF_CRATES, List<List<char>> crates)
        {
            for (int i = 0; i < NUMBER_OF_CRATES; i++)
            {
                crates.Add(new List<char>());
            }
        }

        public static void PrintStacks(List<List<char>> crates, int numberOfCrates)
        {
            for (int i = 0; i < numberOfCrates; i++)
            {
                Console.Write("Stack {0}: ", i + 1);
                crates[i].ForEach(x => Console.Write("{0},", x));
                Console.Write("\n");
            }
        }
    }
}
