import math

arr = [6, 3, 5, 3, 3, 6, 2, 8, 9, 4, 1]

def insertion_sort_by_merging(sorted_subarrays):

    result = []
    pointers = [0] * len(sorted_subarrays)

    for el in sorted_subarrays:
        for i in range(1, len(el)):
            key = el[i]
            j = i - 1
            while j >= 0 and key < el[j]:
                el[j + 1] = el[j]
                j -= 1
            el[j + 1] = key

        

    while sum(pointers) < sum([len(sub) for sub in sorted_subarrays]):
        current_min = float('inf')
        current_min_index = -1
        
        for i in range(len(sorted_subarrays)):
            if pointers[i] < len(sorted_subarrays[i]) and sorted_subarrays[i][pointers[i]] < current_min:
                current_min = sorted_subarrays[i][pointers[i]]
                current_min_index = i
        
        result.append(current_min)
        pointers[current_min_index] += 1


    return result

split_size = 3

subarrays = [arr[i:i+split_size] for i in range(0, len(arr), split_size)]

sorted_subarrays = insertion_sort_by_merging(subarrays)

print(sorted_subarrays)

