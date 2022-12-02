using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day2
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "input.txt";

            Dictionary<string, int> singleValue = new();
            singleValue.Add("X", 
			    1);
            singleValue.Add("Y", 2);
            singleValue.Add("Z", 3);

            Dictionary<(string, string), int> roundValue = new();
            roundValue.Add(("A", "X"), 3);
            roundValue.Add(("B", "Y"), 3);
            roundValue.Add(("C", "Z"), 3);
            roundValue.Add(("A", "Y"), 6);
            roundValue.Add(("B", "Z"), 6);
            roundValue.Add(("C", "X"), 6);
            roundValue.Add(("A", "Z"), 0);
            roundValue.Add(("B", "X"), 0);
            roundValue.Add(("C", "Y"), 0);

            Dictionary<(string, string), string> strategyShape = new();
            strategyShape.Add(("A", "X"), "Z");
            strategyShape.Add(("B", "Y"), "Y");
            strategyShape.Add(("C", "Z"), "X");
            strategyShape.Add(("A", "Y"), "X");
            strategyShape.Add(("B", "Z"), "Z");
            strategyShape.Add(("C", "X"), "Y");
            strategyShape.Add(("A", "Z"), "Y");
            strategyShape.Add(("B", "X"), "X");
            strategyShape.Add(("C", "Y"), "Z");

            // Part one
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                int score = 0;

                while ((line = sr.ReadLine()) != null)
                {
                    var round = line.Split() switch
                    {
                        var a => (a[0], a[1])
                    };

                    score += singleValue[round.Item2] + roundValue[round];
                    Console.WriteLine("Part 1: The Score is {0} points", score);
                }
            }

            // Part two
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                int score = 0;

                while ((line = sr.ReadLine()) != null)
                {
                    var round = line.Split() switch
                    {
                        var a => (a[0], a[1])
                    };

                    var myShape = strategyShape[round];
                    var actualRound = (round.Item1, myShape);
                    score += singleValue[actualRound.Item2] + roundValue[actualRound];
                    Console.WriteLine("Part 2: The Score is {0} points", score);
                }
            }
        }
    }
}
