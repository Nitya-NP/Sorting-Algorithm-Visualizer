""" Main method to run the sort program """

from BubbleSort import BubbleSort
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from BucketSort import BucketSort
from CountingSort import CountingSort
from HeapSort import HeapSort
from RadixSort import RadixSort
from InBuildSort import InBuildSort
from Visualize import Visualizer

sortingOptions = {
    "1": ("Bubble Sort", BubbleSort.bubbleSort),
    "2": ("Selection Sort", SelectionSort.selectionSort),
    "3": ("Insertion Sort", InsertionSort.insertionSort),
    "4": ("Merge Sort", MergeSort.mergeSort),
    "5": ("Quick Sort", QuickSort.quickSort),
    "6": ("Heap Sort", HeapSort.heapSort),
    "7": ("Counting Sort", CountingSort.countingSort),
    "8 ": ("Bucket Sort", BucketSort.bucketSort),
    "9": ("Radix Sort", RadixSort.radixSort),
    "10": ("Python Built-in Sort", InBuildSort.inBuildSort)
}

print("Choose a sorting algorithm to visualize:")
for key, (name, _) in sortingOptions.items():
    print(f"{key}. {name}")

choice = input("Enter the number: ").strip()
if choice in sortingOptions:
    title, sortFunc = sortingOptions[choice]
    arr = [64, 34, 25, 12, 12, 11, 90,15,100,50,66,97,12,11,45,80,1,32]  # default array
    Visualizer.visualize(title, sortFunc, arr.copy())
else:
    print("Invalid choice.")



