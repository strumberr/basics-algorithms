import math


def heapsort(arr):
    n = len(arr)

    def organizeMaxHeap(arr, i, n):
        vl = 2 * i + 1
        vr = 2 * i + 2
        maxIndex = i

        if vl < n and arr[vl] >= arr[maxIndex]:
            maxIndex = vl

        if vr < n and arr[vr] >= arr[maxIndex]:
            maxIndex = vr

        if maxIndex != i:
            arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
            organizeMaxHeap(arr, maxIndex, n)

    for i in range(n // 2 - 1, -1, -1):
        organizeMaxHeap(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        organizeMaxHeap(arr, 0, i)

    return arr


arr = [4, 6, 3, 2, 1, 4, 7, 8, 9, 10]

print(heapsort(arr))