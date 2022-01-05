from queue import PriorityQueue
import numpy as np
import json 

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
