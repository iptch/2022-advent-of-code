using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day3
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "input.txt";

            // Part one
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                int fully_contained_pairs = 0;
                int overlap = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    char[] delimiters = { ',', '-' };
                    int[] num = line.Split(delimiters).Select(x => int.Parse(x)).ToArray();

                    // Part 1
                    if (((num[1] - num[0]) >= (num[3] - num[2]) && (num[2] >= num[0] && num[3] <= num[1])) || num[0] >= num[2] && num[1] <= num[3])
                    {
                        fully_contained_pairs++;
                    }
                    Console.WriteLine("Number of fully contained pairs: {0}", fully_contained_pairs);

                    // Part 2
                    if ((num[2] >= num[0] && num[2] <= num[1]) || (num[0] >= num[2] && num[0] <= num[3]))
                    {
                        overlap++;
                    }

                    Console.WriteLine("Number of overlaps: {0}", overlap);
                }
            }
        }
    }
}
