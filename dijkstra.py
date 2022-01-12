from queue import PriorityQueue
import numpy as np
import time
import json 
import matplotlib.pyplot as plt
 
class Graph:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edges = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visited = []
 
 
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
 
 
    def dijkstra(graph, start):
        D = {v:float('inf') for v in range(graph.v)}
        D[start] = 0
 
        pq = PriorityQueue()
        pq.put((0, start))
 
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            graph.visited.append(current_vertex)
 
            for neighbor in range(graph.v):
                if graph.edges[current_vertex][neighbor] != -1:
                    distance = graph.edges[current_vertex][neighbor]
                    if neighbor not in graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D
 
 
    def generate_random_graph(num_vertices):
        g = Graph(num_vertices)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if j <= i:
                    continue
                weight = np.random.randint(-10, 20)
                if weight < 1:
                    weight = -1
                g.add_edge(i, j, weight)
        return g
 
 
    def generate_testcases(low, high, step):
        data = {}
        data["Graph"] = []
 
        while low < high:
            num_vertices = low
            g = Graph.generate_random_graph()
            data["Graph"].append({
                "Size": num_vertices,
                "Matrix": g.edges,
            })
            low += step
 
        with open("GraphTestCases.txt", "w") as outfile:
            json.dump(data, outfile)
 
    def generate_results(min, max, step):
        current_size = min
        data = {}
        data["Dijsktra"] = []
 
        while current_size <= max:
            print("Current number of nodes: ", current_size)
            test_graph = Graph.generate_random_graph(current_size)
            begin = time.perf_counter()
            Graph.dijkstra(test_graph, 0)
            end = time.perf_counter()
 
            data["Dijsktra"].append({
                "Size": current_size,
                "Time": end - begin
            })
            current_size += step
        with open("results/DijsktraTestResults.txt", "w") as outfile:
            json.dump(data, outfile)
    def read_results():
        size_n = []
        time_n = []
        with open("results/DijsktraTestResults.txt") as fp:
            data = json.load(fp)
        for i in data['Dijsktra']:
            size_n.append(i['Size'])
            time_n.append(i['Time'])
        results = {
            "size_n" : size_n,
            "time_n" : time_n
        }
        return results    

    def draw_graph(results):
        size_n = results["size_n"]
        time_n = results["time_n"]
        fig = plt.figure()
        x = np.linspace(min(size_n),max(size_n),len(size_n))
        y = (x + x**2*np.log(x)) / 1000000
        fig.canvas.set_window_title('Dijkstra algorithm')
        plt.plot(size_n, time_n, 'bo', markersize = 2, label = 'Dijkstra algorithm')  
        plt.plot(x, y, label = 'f(x) = n + E*log(n)', color='red')  
        plt.xscale('linear')
        plt.xlabel('Size of input n')
        plt.ylabel('Execution time(s)')
        plt.title('Dijkstra algorithm')
        plt.legend()
        plt.show()

# Privremena funkcija za testiranje algoritma
def main():
    # Dijkstra implementation with min priority queue is O(V + Elog(V))
    '''
    If the maximum number of edges for a graph with V vertices = V^2 - V
    and with this implementation each vertex has 66% chance to be connected to
    every other vertex, E should be 0.66(V^2 - V) on average
    '''
 
    # print("Generating Dijkstra results")
    # begin = time.perf_counter()
    # Graph.generate_results(10, 600, 10)
    # end = time.perf_counter()
    # print(f"Generation finished in: {end - begin:0.4f}s")
    results = Graph.read_results()
    Graph.draw_graph(results)
 
if __name__ == "__main__":
    main()