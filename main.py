import numpy as np
from dijkstra import Graph
from searchAlgo import *
from fibonacci import *
import time

def main ():
    # Temporary dijkstra test
   
    g = Graph.generate_random_graph(450)
    begin = time.perf_counter()
    print("DIJKSTRA")
    Graph.dijkstra(g, 0)
    # print(Graph.dijkstra(g, 0))
    # print(g.edges)
    end = time.perf_counter()

    print(f"Time to execute: {end - begin:0.4f} s")
    # Graph.generate_testcases(2, 30, 1)


if __name__ == "__main__":
    main()