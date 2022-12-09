using System;
using System.Text;

namespace aoc2022
{
    class day8
    {
        public static void Main(string[] args)
        {
            string filepath = "sample_input.txt";
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

            MoveHeadForAllCommands(commands, headHistory);

            (int x, int y) newTail = new();
            int dx = head.x - tail.x;
            int dy = head.y - tail.y;
            double norm = Math.Sqrt(dx * dx + dy * dy);

            if (norm < 2)
            {
                head = tail;
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
                    if (dx > 0) { newTail.x = tail.x + 1; }
                    if (dx < 0) { newTail.x = tail.x - 1; }
                }
                else if (dx == -2) { }
                else if (dy == 2) { }
                else if (dy == -2) { }
            }

            // Case ||dx2 + dy2|| < 2 => don't move

            //Case dx==0 || dy==0 (default)
            // dx==0
            // dy>0 => y=y+1
            // dy<0 => y=y.1
            // dy==0
            // dx>0 => x=x+1
            // dx<0 => x=x-1

            // Case ||dx2 + dy2|| > 2
            // dy == 2
            // dx > 0 => x=x+1, y=y+1
            // dx < 0 => x=x-1, y=y+1
            // dy == -2
            // dx == 2
            // dx == -2









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

            void moveHead((int, int) head, (char, int) command)
            {

            }

        }
    }

}