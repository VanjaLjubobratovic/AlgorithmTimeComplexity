import time
import json

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


# privremena funkcija za testiranje algoritama
def main():
    print("Generating Fibonacci results")
    begin = time.perf_counter()
    Fibonacci.generate_results(10000, 150000, 5000, 35)
    end = time.perf_counter()
    print(f"Generation finished in: {end - begin:0.4f}s")

if __name__ == "__main__":
    main()
