import time
import json
import matplotlib.pyplot as plt
import numpy as np
class Fibonacci:
    MAX = 10000000

    def fib_non_dynamic(n):
        if n <= 1:
            return 1
        return Fibonacci.fib_non_dynamic(n - 1) + Fibonacci.fib_non_dynamic(n - 2)

    def fib_non_dynamic_list(n):
        fibo_vals = []
        for i in range(n):
            fibo_vals.append(Fibonacci.fib_non_dynamic(i))
        return fibo_vals

    def fib_dynamic(n, list): #list is a bool variable used to set the return of final list
        arr = [1, 1]
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])
        if list == True:
            return arr
        else:
            return arr[-1]

    f = [0] * MAX
    def fib_optimized(n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            Fibonacci.f[n] = 1
            return Fibonacci.f[n]
        if (Fibonacci.f[n]):
            return Fibonacci.f[n]
        if n & 1:
            k = (n + 1) // 2
        else:
            k = n // 2
        
        if (n & 1):
            Fibonacci.f[n] = (Fibonacci.fib_optimized(k) * Fibonacci.fib_optimized(k) + Fibonacci.fib_optimized(k - 1) * Fibonacci.fib_optimized(k - 1))
        else:
            Fibonacci.f[n] = (2 * Fibonacci.fib_optimized(k - 1) + Fibonacci.fib_optimized(k)) * Fibonacci.fib_optimized(k)
        return Fibonacci.f[n]

    def generate_results(min, max, step, max_recursive):
        current_size = min
        data = {}
        data["Naive"] = []
        data["Dynamic"] = []
        data["Optimized"] = []


        for i in range(1, max_recursive + 1, 1):
            print("Current recursive fibonacci input size: ", i)
            begin = time.perf_counter()
            Fibonacci.fib_non_dynamic(i)
            end = time.perf_counter()

            data["Naive"].append({
            "Size": i,
            "Time": float(end - begin)
            })
        
        while current_size <= max:
            print("Current Dynamic and optimized input size: ", current_size)
            begin = time.perf_counter()
            Fibonacci.fib_dynamic(current_size, False)
            end = time.perf_counter()

            data["Dynamic"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            begin = time.perf_counter()
            Fibonacci.fib_optimized(current_size)
            end = time.perf_counter()

            data["Optimized"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })
            current_size += step
        print("Writing data")
        with open("results/FibonacciResults.txt", "w") as outfile:
            json.dump(data, outfile)

    def read_results():
        size_n_naive = []
        time_n_naive = []
        size_n_dynamic= []
        time_n_dynamic = []
        size_n_optimized = []
        time_n_optimized = []
        with open("results/FibonacciResults.txt") as fp:
            data = json.load(fp)
        for i in data['Naive']:
            size_n_naive.append(i['Size'])
            time_n_naive.append(i['Time'])
        for i in data['Dynamic']:
            size_n_dynamic.append(i['Size'])
            time_n_dynamic.append(i['Time'])
        for i in data['Optimized']:
            size_n_optimized.append(i['Size'])
            time_n_optimized.append(i['Time'])
        results = {
            "size_n_naive" : size_n_naive,
            "time_n_naive" : time_n_naive,
            "size_n_dynamic" : size_n_dynamic,
            "time_n_dynamic" : time_n_dynamic,
            "size_n_optimized" : size_n_optimized,
            "time_n_optimized" : time_n_optimized
        }            
        return results  

    def draw_graph(results):
        size_n_naive = results["size_n_naive"]
        time_n_naive = results["time_n_naive"]
        size_n_dynamic = results["size_n_dynamic"]
        time_n_dynamic = results["time_n_dynamic"]
        size_n_optimized = results["size_n_optimized"]
        time_n_optimized = results["time_n_optimized"]
        fig1 = plt.figure(1)
        fig1.canvas.set_window_title('Fibonacci')
        x_naive = np.linspace(min(size_n_naive),max(size_n_naive),len(size_n_naive))
        y_naive = 2**x_naive / 850000000
        x_dynamic = np.linspace(min(size_n_dynamic),max(size_n_dynamic),len(size_n_dynamic))
        y_dynamic = x_dynamic / 250000
        x_optimized = np.linspace(min(size_n_optimized),max(size_n_optimized),len(size_n_optimized))
        y_optimized = np.log(x_optimized) / 15000
        plt.subplot(311)
        plt.plot(size_n_naive, time_n_naive, label = 'Fibonacci naive algorithm', color = 'red')
        plt.plot(x_naive, y_naive, label = 'f(x) = 2^n', color='black', linestyle = 'dashed')  
        plt.xscale('linear')
        plt.legend()
        plt.subplot(312)
        plt.plot(size_n_dynamic, time_n_dynamic, label = 'Fibonacci dynamic algorithm', color = 'blue')
        plt.plot(x_dynamic, y_dynamic, label = 'f(x) = n', color='black', linestyle = 'dashed')
        plt.ylabel('Execution time(s)')
        plt.legend()
        plt.subplot(313)
        plt.plot(size_n_optimized, time_n_optimized, label = 'Fibonacci optimized algorithm', color = 'green')
        plt.plot(x_optimized, y_optimized, label = 'f(x) = log(n)', color='black', linestyle = 'dashed')
        plt.legend()
        plt.xlabel('Size of input n')  
        plt.show()
        
# privremena funkcija za testiranje algoritama
def main():
    # print("Generating Fibonacci results")
    # begin = time.perf_counter()
    # Fibonacci.generate_results(10000, 150000, 5000, 35)
    # end = time.perf_counter()
    # print(f"Generation finished in: {end - begin:0.4f}s")
    results = Fibonacci.read_results()
    Fibonacci.draw_graph(results)
    

if __name__ == "__main__":
    main()
