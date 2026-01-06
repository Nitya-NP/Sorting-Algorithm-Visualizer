""" Merge Sort"""

class MergeSort:
    @staticmethod
    def mergeSort(arr):
        def merge(l, r):
            if l >= r:
                return

            m = (l + r) // 2
            yield from merge(l, m)
            yield from merge(m + 1, r)

            left = arr[l:m + 1]
            right = arr[m + 1:r + 1]

            i = j = 0
            k = l

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
                yield arr

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
                yield arr

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
                yield arr

        yield from merge(0, len(arr) - 1)

                
            
        

