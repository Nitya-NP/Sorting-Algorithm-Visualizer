""" Selection Sort"""

class SelectionSort:
    @staticmethod
    def selectionSort(arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if(arr[j]<arr[i]):
                    arr[i],arr[j]=arr[j],arr[i]
                    yield arr