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

            // Get grid dimensions
            int n = 0;
            int m = 0;
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    n++;
                    m = line.Length;
                }
            }

            // Read vertices
            int numberOfVertices = n * m;
            List<char> vertices = new();
            int startVertexIndex = 0;
            int stopVertexIndex = 0;
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                while ((line = sr.ReadLine()) != null)
                {
                    for (int i = 0; i < line.Length; i++)
                    {
                        if (line[i] == 'S')
                        {
                            startVertexIndex = i;
                            vertices.Add('a');
                        }
                        else if (line[i] == 'E')
                        {
                            stopVertexIndex = i;
                            vertices.Add('z');
                        }
                        else
                        {
                            vertices.Add(line[i]);
                        }
                    }
                }
            }

            // Print vertices
            for (int i = 0; i < vertices.Count(); i++)
            {
                if (i % m == 0)
                {
                    Console.WriteLine();
                }
                Console.Write(vertices[i]);
            }
            Console.WriteLine();

            // Adjacency graph
            int[,] graph = new int[numberOfVertices, numberOfVertices];

            // grid adjacency
            for (int i = 0; i < graph.GetLength(0); i++)
            {
                for (int j = 0; j < graph.GetLength(1); j++)
                {
                    int x_i = i / m;
                    int x_j = j / m;
                    int y_i = i % m;
                    int y_j = j % m;

                    // adjacency
                    if (
                        (Math.Abs(y_j - y_i) < 2 && (x_j == x_i))
                        || (Math.Abs(x_j - x_i) < 2 && (y_j == y_i))
                    )
                    {
                        graph[i, j] = 1;
                    }
                    else
                    {
                        graph[i, j] = 0;
                    }

                    // filter for only ascending
                    if (vertices[j] - vertices[i] > 1)
                    {
                        graph[i, j] = 0;
                    }
                }
            }

            // Print adjacency graph for example vertices
            int row = 1;
            int column = 2;
            int test_index = row * m + column;

            for (int i = 0; i < vertices.Count(); i++)
            {
                if (i % m == 0)
                {
                    Console.WriteLine();
                }

                if (graph[test_index, i] == 1)
                {
                    Console.Write("1");
                }
                else
                {
                    Console.Write("0");
                }
            }
            Console.WriteLine();

            // Dijkstra
            List<int> distance = new(numberOfVertices);
            List<int> previous = new(numberOfVertices);
            List<int> queue = new(numberOfVertices);

            for (int i = 0; i < vertices.Count; i++)
            {
                distance.Add(int.MaxValue);
                queue.Add(i);
            }
            distance[startVertexIndex] = 0;

            while (queue.Count != 0)
            {
                int u = distance.IndexOf(distance.Min());
                queue.RemoveAt(queue.IndexOf(u));
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