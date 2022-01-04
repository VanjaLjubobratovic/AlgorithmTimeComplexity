import json
import numpy as np

def binary_search(value, arr, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binary_search(value, arr, low, mid - 1)
        else:
            return binary_search(value, arr, mid + 1, high)
    else:
        return -1

def linear_search(value, arr):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return i
    return -1

def generate_search_testcases():
    '''
    Svaki objekt u datoteci predstavlja jedan testcase i
    sadrži:
    Inputs -> lista ulaznih vrijednosti
    Size -> velicina ulaza
    Value -> vrijednost koja se traži

    Ideja je da se uvijek traži element na rubovima (worst case)
    '''
    data = {}
    data["Searching Algorithms"] = []
    max = 10000000
    min = 10
    step = 10

    i = min
    while i <= max:
        print(i)
        arr = np.random.randint(i, size=i)
        arr.sort()
        data["Searching Algorithms"].append({
            "Size": i,
            "Inputs": arr.tolist(),
            "Value": int(np.amax(arr))
        })
        i *= step
    with open("SearchingAlgorithms.txt", "w") as outfile:
        json.dump(data, outfile)
