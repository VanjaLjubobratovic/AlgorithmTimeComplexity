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
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3) 

    print(Graph.dijkstra(g, 0))


if __name__ == "__main__":
    main()