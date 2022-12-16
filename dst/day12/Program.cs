using System;
using System.Text;

namespace aoc2022
{
    class day12
    {
        public static void Main(string[] args)
        {
            string filepath = "sample_input.txt";
            // string filepath = "input.txt";

            // Get dimensions
            int height = 0;
            int width = 0;
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    width = line.Length;
                    height++;
                }
            }

            // Initialize array
            char[,] grid = new char[height, width];

            (int x, int y) startcoord = new();
            (int x, int y) endcoord = new();

            // Fill array
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                int i = 0;
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    for (int j = 0; j < line.Length; j++)
                    {
                        if (line[j] == 'S')
                        {
                            startcoord.x = i;
                            startcoord.y = j;
                            grid[i, j] = 'a';
                        }
                        else if (line[j] == 'E')
                        {
                            endcoord.x = i;
                            endcoord.y = j;
                            grid[i, j] = 'z';
                        }
                        else
                        {
                            grid[i, j] = line[j];
                        }

                    }
                    i++;
                }
            }

            // Print array
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    Console.Write("{0}", grid[i, j]);
                }
                Console.WriteLine();
            }

            // Build adjacency graph
            int vertices = height * width;
            int[,] graph = new int[vertices, vertices];
            for (int i = 0; i < vertices; i++)
            {
                for (int j = 0; j < vertices; j++)
                {
                    if (j / width == i / width)
                    {
                        if (Math.Abs(j - i) < 2)
                        {
                            if (grid[i / width, i % width] - grid[j / width, j % width] < 2)
                            {
                                graph[i, j] = 1;
                            }
                            else
                            {
                                graph[i, j] = 0;
                            }
                        }
                    }
                    else if (j % width == i % width)
                    {
                        if (Math.Abs(j / width - i / width) < 2)
                        {
                            if (grid[i / width, i % width] - grid[j / width, j % width] < 2)
                            {
                                graph[i, j] = 1;
                            }
                            else
                            {
                                graph[i, j] = 0;
                            }
                        }
                    }
                }
            }

            // Print adjacency graph for one field
            int row = 1;
            int column = 3;
            int vertex = row * width + column;
            for (int i = 0; i < vertices; i++)
            {
                if (i % width == 0)
                {
                    Console.WriteLine();
                    Console.Write("{0}", graph[vertex, i]);
                }
                else
                {
                    Console.Write("{0}", graph[vertex, i]);
                }
            }
            Console.WriteLine();
            Console.WriteLine();
        }
    }
}