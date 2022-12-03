using System;
using System.IO;
using System.Text;

namespace aoc2022
{
    class day3
    {
        public static void Main(string[] args)
        {
            //string filepath = "sample_input.txt";
            string filepath = "input.txt";

            // Part one
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                int sum = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    int rucksackLenght = line.Length;
                    List<char> firstCompartment = line.Take(rucksackLenght / 2).ToList<char>();
                    List<char> secondCompartment = line.Skip(rucksackLenght / 2).ToList<char>();
                    IEnumerable<char> commonCharacterList = firstCompartment.Intersect(secondCompartment);
                    char commonCharacter = commonCharacterList.First();
                    sum += convertToPriority(commonCharacter);
                    Console.WriteLine("The sum is {0}", sum);
                }
            }

            // Part two
            Console.WriteLine("Part Two");
            using (StreamReader sr = File.OpenText(filepath))
            {
                string? line = "";
                int sum = 0;
                List<string> allLines = new();
                while ((line = sr.ReadLine()) != null)
                {
                    allLines.Add(line);
                }

                for (int i = 0; i < allLines.Count(); i += 3)
                {
                    var commonCharacterList = allLines[i].Intersect(allLines[i + 1]).Intersect(allLines[i + 2]);
                    var commonCharacter = commonCharacterList.FirstOrDefault();
                    sum += convertToPriority(commonCharacter);
                    Console.WriteLine("The sum is {0}", sum);
                }
            }
        }

        public static int convertToPriority(char letter)
        {
            if ((int)letter < 97) //uppercase
            {
                return (int)letter - 38;
            }
            else
            {
                return (int)letter - 96;
            }
        }
    }
}
