import math
import random

def bogoSort(arr):

    total_iterations = 0

    while (isSorted(arr) == False):
        total_iterations += 1
        shuffle(arr)
        
    return arr, total_iterations


def isSorted(arr):

    n = len(arr)

    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            return False
        
    return True


def shuffle(arr):

    n = len(arr)

    for i in range(n-1, 0, -1):
        j = math.floor(random.random() * (i+1))
        arr[i], arr[j] = arr[j], arr[i]


arr = [3, 2, 5, 1, 0, 4]

print(bogoSort(arr))
