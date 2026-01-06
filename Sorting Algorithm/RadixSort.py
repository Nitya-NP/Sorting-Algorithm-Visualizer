""" Radix Sort """

class RadixSort:
    @staticmethod
    def radixSort(arr):
        def counting_sort(exp):
            output = [0] * len(arr)
            count = [0] * 10

            for num in arr:
                index = (num // exp) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(len(arr) - 1, -1, -1):
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                count[index] -= 1

            for i in range(len(arr)):
                arr[i] = output[i]
                yield arr

        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            yield from counting_sort(exp)
            exp *= 10


