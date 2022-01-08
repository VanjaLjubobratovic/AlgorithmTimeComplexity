import random
import numpy as np
import time
import json
import sys
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
        current_size = min
        data = {}
        data["Random pivot random array"] = []
        data["Random pivot reverse array"] = []
        data["Middle pivot random array"] = []
        data["Middle pivot reverse array"] = []
        data["Last pivot random array"] = []
        data["Last pivot reverse array"] = []
        while current_size < max:
            test_rnd_array = Quicksort.generate_random_array(current_size)
            test_rv_array = Quicksort.generate_reverse_array(current_size)
            temp_rnd_array = test_rnd_array
            temp_rv_array = test_rv_array
            begin = time.perf_counter()
            Quicksort.quick_sort_rnd(temp_rnd_array)
            end = time.perf_counter()
            data["Random pivot random array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            temp_rnd_array = test_rnd_array
            temp_rv_array = test_rv_array
            begin = time.perf_counter()
            Quicksort.quick_sort_rnd(temp_rv_array)
            end = time.perf_counter()
            data["Random pivot reverse array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            temp_rnd_array = test_rnd_array
            temp_rv_array = test_rv_array
            begin = time.perf_counter()
            Quicksort.quick_sort_mid(temp_rnd_array)
            end = time.perf_counter()
            data["Middle pivot random array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            temp_rnd_array = test_rnd_array
            temp_rv_array = test_rv_array
            begin = time.perf_counter()
            Quicksort.quick_sort_mid(temp_rv_array)
            end = time.perf_counter()
            data["Middle pivot reverse array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })
            print("here")
            temp_rnd_array = test_rnd_array
            temp_rv_array = test_rv_array
            print(temp_rnd_array)
            begin = time.perf_counter()
            Quicksort.quick_sort_last(temp_rnd_array)
            end = time.perf_counter()
            data["Last pivot random array"].append({
                "Size": current_size,
                "Time": float(end - begin)
            })

            temp_rnd_array = test_rnd_array
            temp_rv_array = test_rv_array
            # begin = time.perf_counter()
            # Quicksort.quick_sort_last(temp_rv_array)
            # end = time.perf_counter()
            # data["Last pivot reverse array"].append({
            #     "Size": current_size,
            #     "Time": float(end - begin)
            # })
            print(current_size)
            current_size += step
        
        with open("QuicksortAlgorithmsResults.txt", "w") as outfile:
            json.dump(data, outfile)

sys.setrecursionlimit(100000)
print("Generating quicksort algorithms results")
begin = time.perf_counter()
Quicksort.generate_results(50000, 100000, 1000)
end = time.perf_counter()
print(f"Generation finished in: {end - begin:0.4f}s")

# arr = Quicksort.generate_random_array(50000)
# begin = time.perf_counter()
# Quicksort.quick_sort_last(arr)
# end = time.perf_counter()
# print(f"Generation finished in: {end - begin:0.4f}s")
# print(arr)

