import random
import time
import json
import matplotlib.pyplot as plt
import numpy as np

class MatrixMultiplication:
    def MatrixMulti(A, B):
        if(len(A[0]) != len(B)):
            return "Invalid matrix dimensions"
        result = [[0 for i in range(len(A[0]))] for j in range(len(B[0]))]

        # iterating by row of A
        for i in range(len(A)):

            # iterating by column by B
            for j in range(len(B[0])):

                # iterating by rows of B
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]                        
        return result

    def generate_random_matrix(n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = random.randint(0, 100) 
        return matrix
    
    #DEPRECATED FUNCTION, no longer reading test cases from json file
    def read_testcases():
        test_cases = []
        with open("MatrixTestCases.txt") as fp:
            data = json.load(fp)
        for i in data['Matrices']:
            test_cases.append(i['Matrix'])
        return test_cases

    def generate_results(low, high, step):
        test_cases = []
        while low < high:
            size_n = low
            mat = MatrixMultiplication.generate_random_matrix(size_n)
            test_cases.append(mat)
            low += step
        data = {}
        data["Results"] = []
        for i in test_cases:
            print("Current matrix size: ", len(i[0]), " * ", len(i[0]))
            begin = time.perf_counter()
            mat = MatrixMultiplication.MatrixMulti(i,i)
            end = time.perf_counter()
            data["Results"].append({
                    "Size": len(i[0]),
                    "Time": (end - begin),
                })
        with open("results/MatrixResults.txt", "w") as outfile:
            json.dump(data, outfile)
            
    def read_results():
        size_n = []
        time_n = []
        with open("results/MatrixResults.txt") as fp:
            data = json.load(fp)
        for i in data['Results']:
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
        y = x**3 / 2350000
        fig.canvas.set_window_title('Matrix multiplication')
        plt.plot(size_n, time_n, 'bo', markersize = 2, label = 'Matrix multiplication algorithm', )  
        plt.plot(x, y, label = 'f(x) = n^3', color='red')  
        plt.xscale('linear')
        plt.xlabel('Size of input n')
        plt.ylabel('Execution time(s)')
        plt.title('Matrix multiplication algorithm')
        plt.legend()
        plt.show()

def main():
    # test_cases = MatrixMultiplication.generate_testcases(2,50,2)
    # begin = time.perf_counter()
    # MatrixMultiplication.generate_results(test_cases)
    # end = time.perf_counter()
    # print(f"Generation finished in: {end - begin:0.4f}s")
    results =MatrixMultiplication.read_results()
    MatrixMultiplication.draw_graph(results)

if __name__ == "__main__":
    main()

