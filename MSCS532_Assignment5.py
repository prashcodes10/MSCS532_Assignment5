# Quicksort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

#Example Usage

arr = [2, 19, 17, 11, 13, 7, 3, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)


#Randomized Quicksort

import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    rest = arr[:pivot_index] + arr[pivot_index+1:]
    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)


#Example Usage

arr = [2, 19, 17, 11, 13, 7, 3, 5]
sorted_arr = randomized_quicksort(arr)
print("Sorted array:", sorted_arr)