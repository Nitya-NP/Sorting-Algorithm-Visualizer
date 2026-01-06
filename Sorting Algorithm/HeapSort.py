""" Heap Sort """

class HeapSort:
    @staticmethod
    def heapSort(arr):
        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                yield arr
                yield from heapify(n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            yield arr
            yield from heapify(i, 0)
