import random
import time


# General search algorithm
def gen_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


# Binary search algorithm
def binary_search(array, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    if high < low:
        return -1

    mid = (low + high) // 2

    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, low, mid - 1)
    else:
        return binary_search(array, target, mid + 1, high)


if __name__ == '__main__':
    # arr = [1, 3, 5, 10]
    # t = 10
    # print("After General Search: ", gen_search(arr, t))
    # print("After Binary Search: ", binary_search(arr, t))

    # Using Time analysis
    # Sorting the List

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for pointer in sorted_list:
        gen_search(sorted_list, pointer)
    end = time.time()
    print("General Search Time = ", (end - start) / length, " seconds")

    start = time.time()
    for pointer in sorted_list:
        binary_search(sorted_list, pointer)
    end = time.time()
    print("Binary Search Time = ", (end - start) / length, " seconds")
