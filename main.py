import numpy as np
from binarySearch import *
from fibonacci import *

def main ():
    ##temporary binary search test
    print("BINARY SEARCH")
    arr = np.random.randint(100, size=50)
    arr[34] = 100
    arr.sort()
    print(arr)
    print(binary_search(100, arr, 0, len(arr) - 1))

    ##temporary fibonaccy test
    print("FIBONACCI NON-DYNAMIC")
    print(fib_non_dynamic_list(20))

if __name__ == "__main__":
    main()