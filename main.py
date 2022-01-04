import numpy as np
from searchAlgo import *
from fibonacci import *

def main ():
    ##temporary binary search test
    print("BINARY SEARCH")
    arr = np.random.randint(100, size=50)
    arr[34] = 25
    arr.sort()
    print(arr)
    print(binary_search(25, arr, 0, len(arr) - 1))

    ##temporary linear search test
    print("LINEAR SEARCH")
    print(linear_search(25, arr))

    ##temporary fibonacci test
    print("FIBONACCI NON-DYNAMIC")
    print(fib_non_dynamic_list(20))

if __name__ == "__main__":
    main()