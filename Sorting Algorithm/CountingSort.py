""" Counting Sort """

class CountingSort:
    @staticmethod
    def countingSort(arr):
        min_val = min(arr)
        max_val = max(arr)

        count = [0] * (max_val - min_val + 1)

        for num in arr:
            count[num - min_val] += 1

        idx = 0
        for i in range(len(count)):
            while count[i] > 0:
                arr[idx] = i + min_val
                idx += 1
                count[i] -= 1
                yield arr
