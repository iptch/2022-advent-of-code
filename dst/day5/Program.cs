using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day5
    {
        public static void Main(string[] args)
        {
            string filepath = "sample_input.txt";
            // string filepath = "input.txt";

            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    char[] delimiters = { ',', '-' };
                    int[] num = line.Split(delimiters).Select(x => int.Parse(x)).ToArray();
                }
            }
        }
    }
}
