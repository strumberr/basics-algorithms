import math


arr = [4, 6, 3, 2, 1, 4, 7, 8, 9, 10]


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
    
    
def generateTreeAndPrint(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        organizeMaxHeap(arr, i, n)

    return arr

print(generateTreeAndPrint(arr))


def insertX(arr, x):

    arr.append(x)

    i = len(arr) - 1

    while i > 0 and arr[i] > arr[(i - 1) // 2]:

        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]

        i = (i - 1) // 2

    return arr

print(insertX(arr, 11))

def eraseMax(arr):
    n = len(arr)
    arr[0], arr[n - 1] = arr[n - 1], arr[0]
    arr.pop()
    organizeMaxHeap(arr, 0, len(arr))
    return arr

# print(eraseMax(arr))


        

















def heapify(arr, index):
    n = len(arr)
    vx = arr[index]
    vl = arr[2 * index + 1] if 2 * index + 1 < n else float('-inf')
    vr = arr[2 * index + 2] if 2 * index + 2 < n else float('-inf')

    if vx > vl and vx > vr:
        return
    
    elif vl < vr:
        arr[index], arr[2 * index + 2] = arr[2 * index + 2], arr[index]
        heapify(arr, 2 * index + 2)

    else:
        arr[index], arr[2 * index + 1] = arr[2 * index + 1], arr[index]
        heapify(arr, 2 * index + 1)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0)

    return arr

# print(heapSort(arr))
    
    