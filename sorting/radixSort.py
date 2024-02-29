import math 
import time


def radixSort(arr):

    max_number = max(arr)

    exp = 1

    iteration = 0
    
    while max_number // exp > 0:

        iteration += 1

        buckets = [[] for _ in range(10)]
        
        for number in arr:
            index = (number // exp) % 10 # example: 170 // 1 % 10 = 0
            # print(f"number: {number}, index: {index}")
            buckets[index].append(number)
      
        arr_index = 0

        for bucket in buckets:
            for number in bucket:

                arr[arr_index] = number

                arr_index += 1

        exp *= 10

        # print(f"{iteration} - arr:", arr)

    
    return arr, iteration


arr = [170, 45, 75, 90, 802, 24, 2, 66, 22, 12, 63, 91, 0, 4, 1000]
radixSort(arr)
print("Sorted array is:", arr)



