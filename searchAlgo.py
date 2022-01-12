import json
import numpy as np
import time
import ijson
import matplotlib.pyplot as plt
class SearchAlgo:
    def binary_search(value, arr, low, high):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] > value:
                return SearchAlgo.binary_search(value, arr, low, mid - 1)
            else:
                return SearchAlgo.binary_search(value, arr, mid + 1, high)
        else:
            return -1

    def linear_search(value, arr):
        for i in range(0, len(arr)):
            if arr[i] == value:
                return i
        return -1

    #OBSOLETE FUNCTION
    def generate_search_testcases(low, high, step):
        #High should be 10 mil max with this implementation
        #low is intended to be 1 mil and step is 100k
        data = {}
        data["Searching Algorithms"] = []

        i = low
        while i <= high:
            print(i)
            arr = np.random.randint(i, size=i)
            arr.sort()
            data["Searching Algorithms"].append({
                "Size": i,
                "Inputs": arr.tolist(),
                "Value": int(np.amax(arr))
            })
            i += step
        with open("SearchingAlgorithms.txt", "w") as outfile:
            json.dump(data, outfile)

    #OBSOLETE FUNCTION
    def read_testcases():
        test_cases = []
        test_case_sizes = []
        test_case_search_values = []
        with open("SearchingAlgorithms.txt", "rb") as infile:
            items = ijson.items(infile, "Searching Algorithms.item")
            for item in items:
                test_cases.append(item["Inputs"])
                test_case_sizes.append(item["Size"])
                test_case_search_values.append(item["Value"])
        return test_cases, test_case_sizes, test_case_search_values


    def generate_array(num_of_elements):
        arr = np.random.randint(num_of_elements, size = num_of_elements)
        arr.sort()
        search_val = int(np.amax(arr))
        return arr, search_val


    def generate_results(min, max, step):
        current_size = min
        data = {}
        data["Binary"] = []
        data["Linear"] = []
        while current_size <= max:
            test_array, search_val = SearchAlgo.generate_array(current_size)
            print("Current array size: ", current_size)
            begin = time.perf_counter()
            SearchAlgo.binary_search(search_val, test_array, 0, current_size - 1)
            end = time.perf_counter()

            data["Binary"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            begin = time.perf_counter()
            SearchAlgo.linear_search(search_val, test_array)
            end = time.perf_counter()

            data["Linear"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })
            current_size += step
        with open("results/SearchingAlgorithmsResults.txt", "w") as outfile:
            json.dump(data, outfile)

    def read_results():
        size_n_bin = []
        time_n_bin = []
        size_n_lin = []
        time_n_lin = []
        with open("results/SearchingAlgorithmsResults.txt") as fp:
            data = json.load(fp)
        for i in data['Binary']:
            size_n_bin.append(i['Size'])
            time_n_bin.append(i['Time'])
        for i in data['Linear']:
            size_n_lin.append(i['Size'])
            time_n_lin.append(i['Time'])
        results = {
            "size_n_bin" : size_n_bin,
            "time_n_bin" : time_n_bin,
            "size_n_lin" : size_n_lin,
            "time_n_lin" : time_n_lin
        }
        return results    

    def draw_graph(results):
        size_n_bin = results["size_n_bin"]
        time_n_bin = results["time_n_bin"]
        size_n_lin = results["size_n_lin"]
        time_n_lin = results["time_n_lin"]
        fig = plt.figure()
        x_bin = np.linspace(min(size_n_bin),max(size_n_bin),len(size_n_bin))
        y_bin = np.log(x_bin) / 350000
        x_lin = np.linspace(min(size_n_lin),max(size_n_lin),len(size_n_lin))
        y_lin = x_lin / 3500000
        fig.canvas.set_window_title('Search algorithms')
        plt.subplot(211)
        plt.plot(size_n_lin, time_n_lin, label = 'Linear search algorithm', color = 'red')  
        plt.plot(x_lin, y_lin, label = 'f(x) = n', color='black', linestyle = 'dotted')
        plt.ylabel('Execution time(s)')
        plt.title('Search algorithms')
        plt.legend()  
        plt.subplot(212)
        plt.plot(size_n_bin, time_n_bin, label = 'Binary search algorithm', color = 'green')
        plt.plot(x_bin, y_bin, label = 'f(x) = log(n)', color='black', linestyle = 'dotted')
        plt.xscale('linear')
        plt.xlabel('Size of input n')
        plt.legend()
        plt.show()
    # privremena funkcija za testiranje algoritama
def main():
    # print("Generating search algorithms results")
    # begin = time.perf_counter()
    # SearchAlgo.generate_results(1000000, 10000000, 100000)
    # end = time.perf_counter()
    # print(f"Generation finished in: {end - begin:0.4f}s")
    results = SearchAlgo.read_results()
    SearchAlgo.draw_graph(results)

if __name__ == "__main__":
    main()