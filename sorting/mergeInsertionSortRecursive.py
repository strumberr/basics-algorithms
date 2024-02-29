import math

arr = [6, 3, 5, 3, 3, 6, 2, 8, 9, 4, 1]


def mergeSort(arr, beg, end):

    if end - beg < 2:
        return

    mid = (beg + end) // 2

    mergeSort(arr, beg, mid)
    mergeSort(arr, mid, end) 
    
    temp = []
    
    i, j = beg, mid

    while i < mid and j < end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1


    while i < mid:
        temp.append(arr[i])
        i += 1


    while j < end:
        temp.append(arr[j])
        j += 1

    for i in range(len(temp)):
        arr[beg + i] = temp[i]

    return arr


print(mergeSort(arr, 0, len(arr)))
            





