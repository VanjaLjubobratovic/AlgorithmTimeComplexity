import numpy as np
from binarySearch import *

def main ():
    ##temporary binary search test
    arr = np.random.randint(100, size=50)
    arr[34] = 100
    arr.sort()
    print(arr)
    print(binary_search(100, arr, 0, len(arr) - 1))

if __name__ == "__main__":
    main()