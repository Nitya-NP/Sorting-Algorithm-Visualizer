""" Quick Sort """

class QuickSort:
    @staticmethod
    def quickSort(arr):
        def quick(low, high):
            if low < high:
                pivot = arr[high]
                i = low
                for j in range(low, high):
                    if arr[j] < pivot:
                        arr[i], arr[j] = arr[j], arr[i]
                        yield arr
                        i += 1
                arr[i], arr[high] = arr[high], arr[i]
                yield arr
                yield from quick(low, i - 1)
                yield from quick(i + 1, high)

        yield from quick(0, len(arr) - 1)


