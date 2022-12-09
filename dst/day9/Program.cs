using System;
using System.Text;

namespace aoc2022
{
    class day8
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "sample_input_2.txt";
            // string filepath = "input.txt";
            List<(char, int)> parsedCommands = new();
            ParseCommands(filepath, parsedCommands);
            List<char> commands = new();
            ExpandCommands(parsedCommands, commands);

            // Initialize Head
            (int x, int y) head;
            (int x, int y) tail;

            // Record History
            List<(int x, int y)> headHistory = new();
            List<(int x, int y)> tailHistory = new();

            // Starting position
            head = (0, 0);
            headHistory.Add(head);
            tail = (0, 0);
            tailHistory.Add(tail);


            // Part 1
            MoveHeadForAllCommands(commands, headHistory);

            foreach ((int x, int y) item in headHistory)
            {
                (int x, int y) oldTail = tailHistory.Last();
                (int x, int y) newTail = updateTail(item, oldTail);
                tailHistory.Add(newTail);
            }

            int uniquePositions = tailHistory.Distinct().Count();
            Console.WriteLine("Unique Positions: {0}", uniquePositions);

            // Part 2

            List<(int x, int y)> tail0 = new() { (0, 0) };
            List<(int x, int y)> tail1 = new() { (0, 0) };
            List<(int x, int y)> tail2 = new() { (0, 0) };
            List<(int x, int y)> tail3 = new() { (0, 0) };
            List<(int x, int y)> tail4 = new() { (0, 0) };
            List<(int x, int y)> tail5 = new() { (0, 0) };
            List<(int x, int y)> tail6 = new() { (0, 0) };
            List<(int x, int y)> tail7 = new() { (0, 0) };
            List<(int x, int y)> tail8 = new() { (0, 0) };
            List<(int x, int y)> tail9 = new() { (0, 0) };

            foreach ((int x, int y) item in headHistory)
            {
                update2(tail0, item);
                update2(tail1, tail0.Last());
                update2(tail2, tail1.Last());
                update2(tail3, tail2.Last());
                update2(tail4, tail3.Last());
                update2(tail5, tail4.Last());
                update2(tail6, tail5.Last());
                update2(tail7, tail6.Last());
                update2(tail8, tail7.Last());
                update2(tail9, tail8.Last());
            }

            int uniquePositionsPart2 = tail9.Distinct().Count();
            Console.WriteLine("Part 2 Unique Positions: {0}", uniquePositionsPart2);
        }
        private static void update2(List<(int x, int y)> tailHistory, (int x, int y) item)
        {
            (int x, int y) oldTail = tailHistory.Last();
            (int x, int y) newTail = updateTail(item, oldTail);
            tailHistory.Add(newTail);
        }

        private static (int x, int y) updateTail((int x, int y) head, (int x, int y) tail)
        {
            (int x, int y) newTail = new();
            int dx = head.x - tail.x;
            int dy = head.y - tail.y;

            if (Math.Abs(dx) <= 1 && Math.Abs(dy) <= 1)
            {
                newTail = tail;
            }
            else if (dx == 0 || dy == 0)
            {
                if (dx == 0)
                {
                    newTail.x = tail.x;
                    if (dy > 0) { newTail.y = tail.y + 1; }
                    if (dy < 0) { newTail.y = tail.y - 1; }
                }
                else if (dy == 0)
                {
                    newTail.y = tail.y;
                    if (dx > 0) { newTail.x = tail.x + 1; }
                    if (dx < 0) { newTail.x = tail.x - 1; }
                }
            }
            else
            {
                if (dx == 2)
                {
                    newTail.x = tail.x + 1;
                    if (dy > 0) { newTail.y = tail.y + 1; }
                    if (dy < 0) { newTail.y = tail.y - 1; }
                }
                else if (dx == -2)
                {
                    newTail.x = tail.x - 1;
                    if (dy > 0) { newTail.y = tail.y + 1; }
                    if (dy < 0) { newTail.y = tail.y - 1; }
                }
                else if (dy == 2)
                {
                    newTail.y = tail.y + 1;
                    if (dx > 0) { newTail.x = tail.x + 1; }
                    if (dx < 0) { newTail.x = tail.x - 1; }
                }
                else if (dy == -2)
                {
                    newTail.y = tail.y - 1;
                    if (dx > 0) { newTail.x = tail.x + 1; }
                    if (dx < 0) { newTail.x = tail.x - 1; }
                }
            }

            return newTail;
        }

        private static void MoveHeadForAllCommands(List<char> commands, List<(int x, int y)> headHistory)
        {
            foreach (char command in commands)
            {
                (int x, int y) newPosition = MoveKnot(headHistory.Last(), command);
                headHistory.Add(newPosition);
            }
        }

        private static (int x, int y) MoveKnot((int x, int y) input, char command)
        {
            (int x, int y) knot = input;
            switch (command)
            {
                case 'L': { knot.x = knot.x - 1; break; };
                case 'R': { knot.x = knot.x + 1; break; };
                case 'U': { knot.y = knot.y + 1; break; };
                case 'D': { knot.y = knot.y - 1; break; };
            }

            return knot;
        }

        private static void ExpandCommands(List<(char, int)> parsedCommands, List<char> commands)
        {
            foreach ((char, int) item in parsedCommands)
            {
                for (int i = 0; i < item.Item2; i++)
                {
                    commands.Add(item.Item1);
                }
            }
        }

        private static void ParseCommands(string filepath, List<(char, int)> commands)
        {
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    (char, int) command;
                    string[] parsed = line.Split();
                    command.Item1 = parsed[0][0];
                    command.Item2 = int.Parse(parsed[1]);
                    commands.Add(command);
                }
            }
        }
    }

}