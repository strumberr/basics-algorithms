import math


def countingSort(arr, maxVal):
    m = maxVal + 1
    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0

    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1

    return arr

print(countingSort([4, 6, 3, 2, 1, 4, 7, 8, 9, 10], 10))
