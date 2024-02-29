import math

def insertionSort(arr):

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:

            arr[j], arr[j - 1] = arr[j - 1], arr[j]

            j -= 1

    return arr


print(insertionSort([5, 7, 2, 1, 4, 6, 3, 8, 9, 10]))

