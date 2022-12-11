using System;
using System.Text;

namespace aoc2022
{
    class day8
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            // const int ROPE_LENGTH = 2;
            // string filepath = "sample_input_2.txt";
            const int ROPE_LENGTH = 10;
            string filepath = "input.txt";

            List<(char, int)> commands = new();
            ParseCommands(filepath, commands);

            // Initialize Rope
            List<(int x, int y)> rope = new();
            for (int i = 0; i < ROPE_LENGTH; i++)
            {
                rope.Add((0, 0));
            }

            // Initialize Tail Positions
            List<(int x, int y)> tailPositions = new();
            tailPositions.Add((0, 0));

            foreach ((char direction, int steps) command in commands)
            {
                for (int i = 0; i < command.steps; i++)
                {
                    (int x, int y) newHeadPosition = GetNewHeadPosition(rope[0], command.direction);
                    rope[0] = newHeadPosition;

                    for (int j = 1; j < ROPE_LENGTH; j++)
                    {
                        (int x, int y) newKnotPosition = GetNewKnotPosition(rope[j - 1], rope[j]);
                        rope[j] = newKnotPosition;
                    }

                    tailPositions.Add(rope[ROPE_LENGTH - 1]);
                }
            }

            Console.WriteLine("Unique tail positions: {0}", tailPositions.Distinct().Count());
        }

        private static (int x, int y) GetNewKnotPosition((int x, int y) frontKnot, (int x, int y) backKnot)
        {
            (int x, int y) newBackKnot = new();
            int dx = frontKnot.x - backKnot.x;
            int dy = frontKnot.y - backKnot.y;

            if (Math.Abs(dx) <= 1 && Math.Abs(dy) <= 1)
            {
                newBackKnot = backKnot;
            }
            else if (dx == 0 || dy == 0)
            {
                if (dx == 0)
                {
                    newBackKnot.x = backKnot.x;
                    if (dy > 0) { newBackKnot.y = backKnot.y + 1; }
                    if (dy < 0) { newBackKnot.y = backKnot.y - 1; }
                }
                else if (dy == 0)
                {
                    newBackKnot.y = backKnot.y;
                    if (dx > 0) { newBackKnot.x = backKnot.x + 1; }
                    if (dx < 0) { newBackKnot.x = backKnot.x - 1; }
                }
            }
            else
            {
                if (dx >= 2)
                {
                    newBackKnot.x = backKnot.x + 1;
                    if (dy > 0) { newBackKnot.y = backKnot.y + 1; }
                    if (dy < 0) { newBackKnot.y = backKnot.y - 1; }
                }
                else if (dx <= -2)
                {
                    newBackKnot.x = backKnot.x - 1;
                    if (dy > 0) { newBackKnot.y = backKnot.y + 1; }
                    if (dy < 0) { newBackKnot.y = backKnot.y - 1; }
                }
                else if (dy >= 2)
                {
                    newBackKnot.y = backKnot.y + 1;
                    if (dx > 0) { newBackKnot.x = backKnot.x + 1; }
                    if (dx < 0) { newBackKnot.x = backKnot.x - 1; }
                }
                else if (dy <= -2)
                {
                    newBackKnot.y = backKnot.y - 1;
                    if (dx > 0) { newBackKnot.x = backKnot.x + 1; }
                    if (dx < 0) { newBackKnot.x = backKnot.x - 1; }
                }
            }

            return newBackKnot;
        }

        private static (int x, int y) GetNewHeadPosition((int x, int y) input, char command)
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