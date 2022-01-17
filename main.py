import numpy as np
from dijkstra import Graph
from searchAlgo import *
from fibonacci import *
from dijkstra import *
from quicksort import *
from matrix_multiplication import *
import time
import matplotlib.pyplot as plt
import os.path

dijkstra_test = False
search_test = False
matrix_test = False
fibonacci_test = False
quicksort_test = False
result_plotting = False

def print_menu(currently_selected):
    if not fibonacci_test:
        print("[1] Fibonacci")
    if not dijkstra_test:
        print("[2] Dijsktra's algorithm")
    if not search_test:
        print("[3] Binary and linear search")
    if not quicksort_test:
        print("[4] Quicksort")
    if not matrix_test:
        print("[5] Matrix multiplication algorithm")
    if not result_plotting:
        print("[6] PLOT SAVED RESULTS")
    print("[0] FINISH SELECTION")

    print(currently_selected)
    if result_plotting:
        print("<--PLOT RESULTS-->")

def execute_algorithms():
    if fibonacci_test:
        print("Generating test results for Fibonacci")
        begin = time.perf_counter()
        Fibonacci.generate_results(10000, 150000, 5000, 35)
        end = time.perf_counter()
        print(f"Generation finished in: {end - begin:0.4f}s\n\n")
    if dijkstra_test:
        print("Generating test results for Dijkstra's algorithm")
        begin = time.perf_counter()
        Graph.generate_results(10, 600, 10)
        end = time.perf_counter()
        print(f"Generation finished in: {end - begin:0.4f}s\n\n")
    if search_test:
        print("Generating test results for Binary and linear search")
        begin = time.perf_counter()
        SearchAlgo.generate_results(1000000, 10000000, 100000)
        end = time.perf_counter()
        print(f"Generation finished in: {end - begin:0.4f}s\n\n")
    if quicksort_test:
        print("Generating test results for quicksort")
        begin = time.perf_counter()
        Quicksort.generate_results(50000, 100000, 1000)
        end = time.perf_counter()
        print(f"Generation finished in: {end - begin:0.4f}s\n\n")
    if matrix_test:
        print("Generating test results for matrix multiplication")
        begin = time.perf_counter()
        MatrixMultiplication.generate_results(2,200,3)
        end = time.perf_counter()
        print(f"Generation finished in: {end - begin:0.4f}s\n\n")

def plot_results():
    if os.path.isfile("results/FibonacciResults.txt"):
        print("Plotting results for Fibonacci...\n")
        Fibonacci.draw_graph(Fibonacci.read_results())
    if os.path.isfile("results/DijsktraTestResults.txt"):
        print("Plotting results for Dijkstra...\n")
        Graph.draw_graph(Graph.read_results())
    if os.path.isfile("results/SearchingAlgorithmsResults.txt"):
        print("Plotting results for binary and linear search...\n")
        SearchAlgo.draw_graph(SearchAlgo.read_results())
    if os.path.isfile("results/QuicksortAlgorithmsResults.txt"):
        print("Plotting results for Quicksort...\n")
        Quicksort.draw_graph(Quicksort.read_results())
    if os.path.isfile("results/MatrixResults.txt"):
        print("Plotting results for matrix multiplication algorithm...\n")
        MatrixMultiplication.draw_graph(MatrixMultiplication.read_results())

def main ():
    global fibonacci_test
    global matrix_test
    global quicksort_test
    global dijkstra_test
    global search_test
    global matrix_test
    global result_plotting
    currently_selected = "--------------\nCurrently selected:"

    print("Select the algorithms you want to execute ()")
    print_menu(currently_selected)
    option = int(input("\nEnter your option: "))

    while option != 0:
        if option == 1:
            fibonacci_test = True
            print("Fibonacci selected\n\n")
            currently_selected += "\nFibonacci"
        elif option == 2:
            dijkstra_test = True
            print("Dijkstra's algorithm selected\n\n")
            currently_selected += "\nDijkstra's algorithm"
        elif option == 3:
            search_test = True
            print("Binary and linear search selected\n\n")
            currently_selected += "\nBinary and linear search"
        elif option == 4:
            quicksort_test = True
            print("Quicksort selected\n")
            currently_selected += "\nQuicksort"
        elif option == 5:
            matrix_test = True
            print("Matrix multiplication selected\n\n")
            currently_selected += "\nMatrix multiplication"
        elif option == 6:
            result_plotting = True
            print("Result plotting selected")
        else:
            print("Invalid choice, please try again\n\n")
        print_menu(currently_selected)
        option = int(input("\nEnter your option: "))

    execute_algorithms()
    if result_plotting:
        plot_results()

if __name__ == "__main__":
    main()