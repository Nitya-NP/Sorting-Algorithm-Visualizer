""" Bucket Sort """

class BucketSort:
    @staticmethod
    def bucketSort(arr):
        if not arr:
            return

        n = len(arr)
        buckets = [[] for _ in range(n)]
        max_val = max(arr)

        for num in arr:
            idx = int(n * num / (max_val + 1))
            buckets[idx].append(num)

        i = 0
        for bucket in buckets:
            bucket.sort()
            for num in bucket:
                arr[i] = num
                i += 1
                yield arr

