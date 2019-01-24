from selection import selectionSort
from bubble import bubbleSort
from merge import mergeSort
from tim import timSort

import time
import random
import matplotlib.pyplot as plt

def measure_sort(lengths_of_lists, algorithm, max_int=10000):
    elapsed_times = []
    for length in lengths_of_lists:
        alist = [random.randint(0, max_int) for i in range(length)]
        start = time.time()
        algorithm(alist)
        end = time.time()
        elapsed_times.append(end - start)
    
    return [lengths_of_lists, elapsed_times]

lengths = [10, 20, 30, 50, 100, 200, 500, 800, 1500, 2500]

selection_sort_times = measure_sort(lengths, selectionSort)
bubble_sort_times = measure_sort(lengths, bubbleSort)
merge_sort_times = measure_sort(lengths, mergeSort)
tim_sort_times = measure_sort(lengths, timSort)

plt.plot(*selection_sort_times)
plt.plot(*bubble_sort_times)
plt.plot(*merge_sort_times)
plt.plot(*tim_sort_times)
plt.title("Relations between length of lists and the elapsed time")
plt.xlabel("Lengths of Lists")
plt.ylabel("Elapsed Time [sec]")
plt.legend(["selection sort", "bubble sort", "merge sort", "tim sort"])
plt.show()