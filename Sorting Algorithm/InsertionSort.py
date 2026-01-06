""" Insertion Sort """

class InsertionSort:
    @staticmethod
    def insertionSort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                yield arr
            arr[j+1] = key
        yield arr

