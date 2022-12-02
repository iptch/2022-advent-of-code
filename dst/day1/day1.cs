using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day1
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "input.txt";

            List<int> caloryListPerElf = new();
            List<int> totalCaloriesPerElf = new();

            Console.WriteLine("PART ONE");
            ParseInput(filepath, caloryListPerElf, totalCaloriesPerElf);

            Console.WriteLine("Maximum Calories: {0}", totalCaloriesPerElf.Max());
            Console.WriteLine("PART TWO");

            List<int> TotalTopThreeCalories = totalCaloriesPerElf
                .OrderByDescending(value => value)
                .Take(3)
                .ToList();
            ;

            // TotalTopThreeCalories.ForEach(x => Console.WriteLine("Top: {0}", x));
            Console.WriteLine("Total top three calories: {0}", TotalTopThreeCalories.Sum());
        }

        private static void ParseInput(
            string filepath,
            List<int> caloryListPerElf,
            List<int> totalCaloriesPerElf
        )
        {
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? s = "";

                // Read first line
                while ((s = sr.ReadLine()) != null)
                {
                    if (s == "")
                    {
                        // Console.WriteLine("Total Calories: {0}", caloryListPerElf.Sum());
                        totalCaloriesPerElf.Add(caloryListPerElf.Sum());
                        caloryListPerElf.Clear();
                    }
                    else
                    {
                        int value = int.Parse(s);
                        caloryListPerElf.Add(value);
                    }
                }
            }
        }
    }
}
