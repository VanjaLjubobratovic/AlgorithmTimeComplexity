import random

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
            split_index = partition_mid(items, low, high)
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
            split_index = partition_rnd(items, low, high)
            _quick_sort_rnd(items, low, split_index)
            _quick_sort_rnd(items, split_index + 1, high)

    _quick_sort_rnd(nums, 0, len(nums) - 1) 
 
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort_mid(arr)
print("Sorted array with pivot as middle element is:")
for i in range(n):
    print("%d" % arr[i])

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort_rnd(arr)
print("Sorted array with pivot as random element is:")
for i in range(n):
    print("%d" % arr[i])