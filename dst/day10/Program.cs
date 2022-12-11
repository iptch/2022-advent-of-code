using System;
using System.Text;

namespace aoc2022
{
    class day10
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            // string filepath = "small_sample.txt";
            string filepath = "input.txt";
            List<long> resultCycles = new() { 20, 60, 100, 140, 180, 220 };
            List<long> signalStrength = new();
            long cycle = 0;
            long x = 1;

            Console.WriteLine("Start Drawing");
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                int lineNumber = 1;
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    if (line == "noop")
                    {
                        CheckCycleAndIncrement(resultCycles, ref cycle, x, lineNumber, signalStrength);
                    }
                    else
                    {
                        string[] parsed = line.Split();
                        int inputNumber = int.Parse(parsed[1]);

                        CheckCycleAndIncrement(resultCycles, ref cycle, x, lineNumber, signalStrength);
                        CheckCycleAndIncrement(resultCycles, ref cycle, x, lineNumber, signalStrength);
                        x = x + inputNumber;
                    }
                    lineNumber++;
                }
            }

            Console.Write("\n");
            // Console.WriteLine("Sum of signal strength {0}", signalStrength.Sum());
        }

        private static void CheckCycleAndIncrement(List<long> resultCycles, ref long cycle, long x, int lineNumber, List<long> signalStrength)
        {
            if (resultCycles.Contains(cycle))
            {
                // Console.WriteLine("Cycle {0}, x={1}, Signal Strength {2}, Line Number {3}", cycle, x, cycle * x, lineNumber);
                signalStrength.Add(cycle * x);
            }

            if (resultCycles.Contains(cycle - 20))
            {
                Console.Write("\n");
            }

            // Drawing
            if (Math.Abs(cycle % 40 - x) < 2)
            {
                Console.Write("#");
            }
            else
            {
                Console.Write(".");
            }
            cycle++;
        }
    }
}