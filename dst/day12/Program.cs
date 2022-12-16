using System;
using System.Text;

namespace aoc2022
{
    class day12
    {
        public static void Main(string[] args)
        {
            // string filepath = "sample_input.txt";
            string filepath = "input.txt";

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
            List<char> vertexValue = new();
            int startVertexIndex = 0;
            int stopVertexIndex = 0;
            using (StreamReader sr = System.IO.File.OpenText(filepath))
            {
                string? line = "";
                int linenumber = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    for (int i = 0; i < line.Length; i++)
                    {
                        if (line[i] == 'S')
                        {
                            startVertexIndex = m * linenumber + i;
                            vertexValue.Add('a');
                        }
                        else if (line[i] == 'E')
                        {
                            stopVertexIndex = m * linenumber + i;
                            vertexValue.Add('z');
                        }
                        else
                        {
                            vertexValue.Add(line[i]);
                        }
                    }
                    linenumber++;
                }
            }

            // Print vertices
            for (int i = 0; i < vertexValue.Count(); i++)
            {
                if (i % m == 0)
                {
                    Console.WriteLine();
                }
                Console.Write(vertexValue[i]);
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
                    if (vertexValue[j] - vertexValue[i] > 1)
                    {
                        graph[i, j] = 0;
                    }
                }
            }

            // Print adjacency graph for example vertices
            int row = 1;
            int column = 2;
            int test_index = row * m + column;

            for (int i = 0; i < vertexValue.Count(); i++)
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
            // vertexValues
            List<int> vertexDistance = new();
            List<int?> previousVertex = new();
            List<int> vertexQueue = new();

            for (int i = 0; i < vertexValue.Count; i++)
            {
                vertexDistance.Add(int.MaxValue);
                previousVertex.Add(null);
                vertexQueue.Add(i);
            }
            vertexDistance[startVertexIndex] = 0;

            while (vertexQueue.Any())
            {
                int minDist = int.MaxValue;
                int minVertex = 0;
                for (int i = 0; i < vertexQueue.Count; i++)
                {
                    if (vertexDistance[vertexQueue[i]] < minDist)
                    {
                        minDist = vertexDistance[vertexQueue[i]];
                        minVertex = vertexQueue[i];
                    }
                }
                int u = minVertex;
                vertexQueue.Remove(u);
                Console.WriteLine("Still in queue: {0}", vertexQueue.Count);
                foreach (int v in vertexQueue)
                {
                    if (graph[u, v] == 1)
                    {
                        int alt = vertexDistance[u] + 1;
                        if (alt < vertexDistance[v])
                        {
                            vertexDistance[v] = alt;
                            previousVertex[v] = u;
                        }
                    }
                }
            }

            //Backtrack for specific vertex
            int endVertex = stopVertexIndex;
            List<int?> backtrackList = new();
            backtrackList.Add(endVertex);
            int currentVertex = endVertex;
            while (previousVertex[currentVertex] != startVertexIndex)
            {
                backtrackList.Add(previousVertex[currentVertex]);
                currentVertex = (int)previousVertex[currentVertex];
            }
            backtrackList.Add(startVertexIndex);

            for (int i = 0; i < vertexValue.Count(); i++)
            {
                if (i % m == 0)
                {
                    Console.WriteLine();
                }

                if (backtrackList.Contains(i))
                {
                    Console.Write("X");
                }
                else
                {
                    Console.Write(".");
                }
            }
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Distance to StopVertex: {0}", vertexDistance[stopVertexIndex]);
        }
    }
}
