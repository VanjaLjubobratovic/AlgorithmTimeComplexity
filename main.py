import numpy as np
from dijkstra import Graph
from searchAlgo import *
from fibonacci import *
import time

def main ():
    # ##temporary binary search test
    # print("BINARY SEARCH")
    # arr = np.random.randint(100, size=100)
    # arr[34] = 25
    # arr.sort()
    # # print(arr)
    # print(binary_search(25, arr, 0, len(arr) - 1))

    # temporary linear search test
    # print("LINEAR SEARCH")
    # print(linear_search(25, arr))

    # temporary fibonacci test
    # n = 20
    # begin = time.perf_counter()
    # print("FIBONACCI NON-DYNAMIC")
    # print(fib_non_dynamic(n-1))
    # end = time.perf_counter()

    # print(f"Time to execute: {end - begin:0.4f} s")


    # begin = time.perf_counter()
    # print("FIBONACCI DYNAMIC")
    # print(fib_dynamic(n, False))
    # end = time.perf_counter()

    # print(f"Time to execute: {end - begin:0.4f} s")

    # begin = time.perf_counter()
    # print("FIBONACCI OPTIMIZED")
    # print(fib_optimized(n))
    # end = time.perf_counter()

    # print(f"Time to execute: {end - begin:0.4f} s")

    # generate_search_testcases()


    # Temporary dijkstra test
   
    g = Graph.generate_random_graph(1000)
    begin = time.perf_counter()
    print("DIJKSTRA")
    Graph.dijkstra(g, 0)
    #print(Graph.dijkstra(g, 0))
    #print(g.edges)
    end = time.perf_counter()

    print(f"Time to execute: {end - begin:0.4f} s")
    # Graph.generate_testcases(2, 30, 1)


if __name__ == "__main__":
    main()