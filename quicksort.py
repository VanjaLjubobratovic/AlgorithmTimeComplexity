import random
import numpy as np
import time
import json
import sys
import matplotlib.pyplot as plt
class Quicksort:
    def partition_last(nums, low, high):
        pivot = nums[high-1]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            nums[i], nums[j] = nums[j], nums[i]

    def quick_sort_last(nums):
        # Create a helper function that will be called recursively
        def _quick_sort_last(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = Quicksort.partition_last(items, low, high)
                _quick_sort_last(items, low, split_index)
                _quick_sort_last(items, split_index + 1, high)

        _quick_sort_last(nums, 0, len(nums) - 1)

    def partition_mid(nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            nums[i], nums[j] = nums[j], nums[i]

    def quick_sort_mid(nums):
        # Create a helper function that will be called recursively
        def _quick_sort_mid(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = Quicksort.partition_mid(items, low, high)
                _quick_sort_mid(items, low, split_index)
                _quick_sort_mid(items, split_index + 1, high)

        _quick_sort_mid(nums, 0, len(nums) - 1)

    def partition_rnd(nums, low, high):
        pivot = nums[random.randint(low, high)]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            nums[i], nums[j] = nums[j], nums[i]


    def quick_sort_rnd(nums):
        # Create a helper function that will be called recursively
        def _quick_sort_rnd(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = Quicksort.partition_rnd(items, low, high)
                _quick_sort_rnd(items, low, split_index)
                _quick_sort_rnd(items, split_index + 1, high)

        _quick_sort_rnd(nums, 0, len(nums) - 1) 

    def generate_random_array(num_of_elements):
        arr = np.random.randint(num_of_elements, size = num_of_elements)
        return arr

    def generate_reverse_array(num_of_elements):
        arr = np.random.randint(num_of_elements, size = num_of_elements)
        arr.sort()
        reverse_arr = arr[::-1]
        return reverse_arr    

    def generate_results(min, max, step):
        sys.setrecursionlimit(100000)
        current_size = min
        data = {}
        data["Random pivot random array"] = []
        data["Random pivot reverse array"] = []
        data["Middle pivot random array"] = []
        data["Middle pivot reverse array"] = []
        data["Last pivot random array"] = []
        data["Last pivot reverse array"] = []
        while current_size < max:

            print("Current array size: ", current_size)
            #Quicksort with random pivot and random array as input
            test_rnd_array = Quicksort.generate_random_array(current_size)
            begin = time.perf_counter()
            Quicksort.quick_sort_rnd(test_rnd_array)
            end = time.perf_counter()
            data["Random pivot random array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            #Quicksort with random pivot and reverse sorted array as input
            test_rv_array = Quicksort.generate_reverse_array(current_size)
            begin = time.perf_counter()
            Quicksort.quick_sort_rnd(test_rv_array)
            end = time.perf_counter()
            data["Random pivot reverse array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            #Quicksort with middle element as pivot and random array as input
            test_rnd_array = Quicksort.generate_random_array(current_size)
            begin = time.perf_counter()
            Quicksort.quick_sort_mid(test_rnd_array)
            end = time.perf_counter()
            data["Middle pivot random array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            #Quicksort with middle element as pivot and reverse sorted array as input
            test_rv_array = Quicksort.generate_reverse_array(current_size)
            begin = time.perf_counter()
            Quicksort.quick_sort_mid(test_rv_array)
            end = time.perf_counter()
            data["Middle pivot reverse array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            #Quicksort with last element as pivot and random array as input
            test_rnd_array = Quicksort.generate_random_array(current_size)
            begin = time.perf_counter()
            Quicksort.quick_sort_last(test_rnd_array)
            end = time.perf_counter()
            data["Last pivot random array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            #Quicksort with last element as pivot and reverse sorted array as input
            test_rv_array = Quicksort.generate_reverse_array(current_size//20)
            begin = time.perf_counter()
            Quicksort.quick_sort_last(test_rv_array)
            end = time.perf_counter()
            data["Last pivot reverse array"].append({
                "Size": current_size//20,
                "Time": float(end - begin)
            })
            current_size += step
        
        with open("results/QuicksortAlgorithmsResults.txt", "w") as outfile:
            json.dump(data, outfile)
        
    def read_results():
        size_n_rp_rnd = []
        time_n_rp_rnd = []
        size_n_rp_rev= []
        time_n_rp_rev = []
        size_n_mp_rnd = []
        time_n_mp_rnd = []
        size_n_mp_rev = []
        time_n_mp_rev = []
        size_n_lp_rnd = []
        time_n_lp_rnd = []
        size_n_lp_rev = []
        time_n_lp_rev = []

        with open("results/QuicksortAlgorithmsResults.txt") as fp:
            data = json.load(fp)
        for i in data['Random pivot random array']:
            size_n_rp_rnd.append(i['Size'])
            time_n_rp_rnd.append(i['Time'])
        for i in data['Random pivot reverse array']:
            size_n_rp_rev.append(i['Size'])
            time_n_rp_rev.append(i['Time'])
        for i in data['Middle pivot random array']:
            size_n_mp_rnd.append(i['Size'])
            time_n_mp_rnd.append(i['Time'])
        for i in data['Middle pivot reverse array']:
            size_n_mp_rev.append(i['Size'])
            time_n_mp_rev.append(i['Time'])
        for i in data['Last pivot random array']:
            size_n_lp_rnd.append(i['Size'])
            time_n_lp_rnd.append(i['Time'])
        for i in data['Last pivot reverse array']:
            size_n_lp_rev.append(i['Size'])
            time_n_lp_rev.append(i['Time'])
        results = {
            "size_n_rp_rnd" : size_n_rp_rnd,
            "time_n_rp_rnd" : time_n_rp_rnd,
            "size_n_rp_rev" : size_n_rp_rev,
            "time_n_rp_rev" : time_n_rp_rev,
            "size_n_mp_rnd" : size_n_mp_rnd,
            "time_n_mp_rnd" : time_n_mp_rnd,
            "size_n_mp_rev" : size_n_mp_rev,
            "time_n_mp_rev" : time_n_mp_rev,
            "size_n_lp_rnd" : size_n_lp_rnd,
            "time_n_lp_rnd" : time_n_lp_rnd,
            "size_n_lp_rev" : size_n_lp_rev,
            "time_n_lp_rev" : time_n_lp_rev
        }            
        return results

    def draw_graph(results):
        size_n_rp_rnd = results["size_n_rp_rnd"]
        time_n_rp_rnd = results["time_n_rp_rnd"]
        size_n_rp_rev = results["size_n_rp_rev"]
        time_n_rp_rev = results["time_n_rp_rev"]
        size_n_mp_rnd = results["size_n_mp_rnd"]
        time_n_mp_rnd = results["time_n_mp_rnd"]
        size_n_mp_rev = results["size_n_mp_rev"]
        time_n_mp_rev = results["time_n_mp_rev"]
        size_n_lp_rnd = results["size_n_lp_rnd"]
        time_n_lp_rnd = results["time_n_lp_rnd"]
        size_n_lp_rev = results["size_n_lp_rev"]
        time_n_lp_rev = results["time_n_lp_rev"]
        fig1 = plt.figure(1)
        fig1.canvas.set_window_title('Quicksort algorithm')
        x = np.linspace(min(size_n_rp_rnd),max(size_n_rp_rnd),len(size_n_rp_rnd))
        y = x * np.log(x) / 1000000
        plt.subplot(211)
        plt.plot(size_n_rp_rnd, time_n_rp_rnd, label = 'Random pivot random array', color = 'red')
        plt.plot(size_n_mp_rnd, time_n_mp_rnd, label = 'Middle pivot random array', color = 'blue')
        plt.plot(size_n_lp_rnd, time_n_lp_rnd, label = 'Last pivot random array', color = 'green')
        plt.plot(x, y, label = 'f(x) = n * log(n)', color='black', linestyle = 'dashed')
        plt.ylabel('Execution time(s)')  
        plt.xscale('linear')
        plt.legend()
        plt.subplot(212)
        plt.plot(size_n_rp_rev, time_n_rp_rev, label = 'Random pivot reversed array', color = 'red')
        plt.plot(size_n_mp_rev, time_n_mp_rev, label = 'Middle pivot reversed array', color = 'blue')
        plt.plot(size_n_lp_rev, time_n_lp_rev, label = 'Last pivot reversed array', color = 'green')
        plt.plot(x, y, label = 'f(x) = n * log(n)', color='black', linestyle = 'dashed')
        plt.legend()
        plt.xlabel('Size of input n')
        plt.show()        
        

def main():
    # sys.setrecursionlimit(100000)
    # print("Generating quicksort algorithms results")
    # begin = time.perf_counter()
    # Quicksort.generate_results(10, 100000, 1000)
    # end = time.perf_counter()
    # print(f"Generation finished in: {end - begin:0.4f}s")
    results = Quicksort.read_results()
    Quicksort.draw_graph(results)
if __name__ == "__main__":
    main()
