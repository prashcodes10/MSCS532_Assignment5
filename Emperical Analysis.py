#Emperical Analysis

import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10**6)


# Deterministic Quicksort (last element as pivot)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Randomized Quicksort (random pivot)
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    rest = arr[:pivot_index] + arr[pivot_index+1:]
    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Timing function
def time_sort(func, arr):
    start = time.time()
    func(arr.copy())  
    return time.time() - start

# Test input sizes
sizes = [500, 1000, 1500, 2000, 2500]

# Storing results
results = {
    "random": {"det": [], "rand": []},
    "sorted": {"det": [], "rand": []},
    "reverse": {"det": [], "rand": []}
}

for size in sizes:
    random_input = random.sample(range(size * 10), size)
    sorted_input = sorted(random_input)
    reverse_input = sorted_input[::-1]

    # Time deterministic quicksort
    results["random"]["det"].append(time_sort(quicksort, random_input))
    results["sorted"]["det"].append(time_sort(quicksort, sorted_input))
    results["reverse"]["det"].append(time_sort(quicksort, reverse_input))

    # Time randomized quicksort
    results["random"]["rand"].append(time_sort(randomized_quicksort, random_input))
    results["sorted"]["rand"].append(time_sort(randomized_quicksort, sorted_input))
    results["reverse"]["rand"].append(time_sort(randomized_quicksort, reverse_input))

# --- Plotting ---
plt.figure(figsize=(12, 8))

# Random input
plt.plot(sizes, results["random"]["det"], marker='o', label='Deterministic - Random')
plt.plot(sizes, results["random"]["rand"], marker='o', linestyle='--', label='Randomized - Random')

# Sorted input
plt.plot(sizes, results["sorted"]["det"], marker='s', label='Deterministic - Sorted')
plt.plot(sizes, results["sorted"]["rand"], marker='s', linestyle='--', label='Randomized - Sorted')

# Reverse input
plt.plot(sizes, results["reverse"]["det"], marker='^', label='Deterministic - Reverse')
plt.plot(sizes, results["reverse"]["rand"], marker='^', linestyle='--', label='Randomized - Reverse')

plt.title('Empirical Comparison of Deterministic vs Randomized Quicksort')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
