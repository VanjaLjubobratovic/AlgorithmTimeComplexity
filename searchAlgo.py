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