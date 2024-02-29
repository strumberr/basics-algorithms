import math

class QuickSort:
    def __init__(self, arr):
        self.arr = arr


    def quickSortRecursive(self, arr, beg, end):

        if end - beg < 2:
            return

        pivotIndex = (beg + end) // 2

        pivot = arr[pivotIndex]
        arr[pivotIndex], arr[end - 1] = arr[end - 1], arr[pivotIndex]

        i = beg

        for j in range(beg, end - 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                
        arr[i], arr[end - 1] = arr[end - 1], arr[i]

        self.quickSortRecursive(arr, beg, i)
        self.quickSortRecursive(arr, i + 1, end)

        return arr


arr = [3, 5, 2, 1, 4, 6, 7, 8, 9, 10]
print(QuickSort(arr).quickSortRecursive(arr, 0, len(arr)))