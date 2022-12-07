using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day6
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "input.txt";

            // Part 1
            // const int WINDOW_SIZE = 4;
            // Part 2
            const int WINDOW_SIZE = 14;

            int marker = 0;

            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    List<char> list = new List<char>(line);
                    int j = 0;
                    for (int i = 0; i < list.Count() - WINDOW_SIZE; i++)
                    {
                        j = i + WINDOW_SIZE;
                        var count = list.GetRange(i, WINDOW_SIZE).ToHashSet().Count();
                        if (count == WINDOW_SIZE)
                        {
                            marker = j;
                            break;
                        }
                    }
                }
            }
            Console.WriteLine(marker);
        }
    }
}
