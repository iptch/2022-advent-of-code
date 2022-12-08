using System;
using System.Text;

namespace aoc2022
{
    class day8
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "input.txt";

            (int, int) dim = ParseDimensions(filepath);
            Console.WriteLine("Dimensions: ({0}, yDim: {0})", dim.Item1, dim.Item2);
            int[,] grid = new int[dim.Item1, dim.Item2];
            ParseGrid(filepath, grid);
            printGrid(grid);
            int[,] visible = new int[dim.Item1, dim.Item2];

            int visibilitySum = 0;
            int scenicHighScore = 0;
            //Check if element is visible
            for (int i = 0; i < grid.GetLength(0); i++)
            {
                for (int j = 0; j < grid.GetLength(1); j++)
                {
                    // Part 1
                    int visibility = checkVisibility(grid, i, j);
                    visibilitySum += visibility;

                    // Part 2
                    int scenicValue = getScenicScore(grid, i, j);
                    if (scenicValue > scenicHighScore)
                    {
                        scenicHighScore = scenicValue;
                    }
                }
            }

            Console.WriteLine("The visibility sum is {0}", visibilitySum);
            Console.WriteLine("The scenic high score is {0}", scenicHighScore);
        }

        private static int checkVisibility(int[,] grid, int row, int column)
        {
            int thisTree = grid[row, column];
            int sightRight = 0;
            int biggestRight = -1;
            for (int j = column + 1; j < grid.GetLength(1); j++)
            {
                if (biggestRight < grid[row, j])
                {
                    biggestRight = grid[row, j];
                }

                if (grid[row, column] > grid[row, j])
                {
                    sightRight++;
                }
            }

            int biggestLeft = -1;
            int sightLeft = 0;
            for (int j = column - 1; j >= 0; j--)
            {
                if (biggestLeft < grid[row, j])
                {
                    biggestLeft = grid[row, j];
                }

                if (grid[row, column] > grid[row, j])
                {
                    sightLeft++;
                }
            }

            int biggestTop = -1;
            int sightTop = 0;
            for (int i = row - 1; i >= 0; i--)
            {
                if (biggestTop < grid[i, column])
                {
                    biggestTop = grid[i, column];
                }

                if (grid[row, column] > grid[i, column])
                {
                    sightTop++;
                }
            }

            int biggestBottom = -1;
            int sightBottom = 0;
            for (int i = row + 1; i < grid.GetLength(0); i++)
            {
                if (biggestBottom < grid[i, column])
                {
                    biggestBottom = grid[i, column];
                }

                if (grid[row, column] > grid[column, i])
                {
                    sightBottom++;
                }
            }

            int visibility = 0;
            if (thisTree > biggestRight || thisTree > biggestLeft || thisTree > biggestBottom || thisTree > biggestTop)
            {
                visibility = 1;
            }

            int scenicScore = 0;
            scenicScore = sightBottom * sightLeft * sightRight * sightTop;
            return visibility;
        }

        private static int getScenicScore(int[,] grid, int row, int column)
        {
            int sightRight = 0;
            int sightLeft = 0;
            int sightTop = 0;
            int sightBottom = 0;

            //Go Right
            for (int j = column + 1; j < grid.GetLength(1); j++)
            {
                sightRight++;
                if (grid[row, j] >= grid[row, column])
                {
                    break;
                }
            }

            //Go Left
            for (int j = column - 1; j >= 0; j--)
            {
                sightLeft++;
                if (grid[row, j] >= grid[row, column])
                {
                    break;
                }
            }

            //Go Up
            for (int i = row - 1; i >= 0; i--)
            {
                sightTop++;
                if (grid[i, column] >= grid[row, column])
                {
                    break;
                }
            }

            //Go Down
            for (int i = row + 1; i < grid.GetLength(0); i++)
            {
                sightBottom++;
                if (grid[i, column] >= grid[row, column])
                {
                    break;
                }
            }

            int scenicScore = sightBottom * sightLeft * sightRight * sightTop;
            return scenicScore;
        }

        private static void ParseGrid(string filepath, int[,] grid)
        {
            int rowIndex = 0;
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    for (int i = 0; i < grid.GetLength(1); i++)
                    {
                        grid[rowIndex, i] = int.Parse(line[i].ToString());
                    }
                    rowIndex++;
                }
            }
        }

        private static (int, int) ParseDimensions(string filepath)
        {
            (int, int) dim = (0, 0);
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    dim.Item2 = line.Length;
                    dim.Item1++;
                }
            }
            return dim;
        }

        private static void printGrid(int[,] grid)
        {
            for (int i = 0; i < grid.GetLength(0); i++)
            {
                for (int j = 0; j < grid.GetLength(1); j++)
                {
                    Console.Write("{0} ", grid[i, j]);
                }
                Console.WriteLine();
            }
        }
    }
}

