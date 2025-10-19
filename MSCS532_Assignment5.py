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
