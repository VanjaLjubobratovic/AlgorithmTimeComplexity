import numpy as np
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
    begin = time.perf_counter()
    print("FIBONACCI NON-DYNAMIC")
    print(fib_non_dynamic_list(35))
    # fib_non_dynamic(33)
    end = time.perf_counter()

    print(f"Time to execute: {end - begin:0.4f} s")


    begin = time.perf_counter()
    print("FIBONACCI DYNAMIC")
    print(fib_dynamic(35, True))
    end = time.perf_counter()

    print(f"Time to execute: {end - begin:0.4f} s")

    # generate_search_testcases()

if __name__ == "__main__":
    main()