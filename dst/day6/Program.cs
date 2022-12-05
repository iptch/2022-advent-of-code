using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day6
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

                }
            }
        }
    }
}
