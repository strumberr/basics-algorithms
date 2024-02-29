import math 

def binarySearch(arr, x):
        
        left = 0
        right = len(arr) - 1
        iteration = 0
        
        while left <= right:
            
            iteration += 1
            
            mid = left + (right - left) // 2
            
            if arr[mid] == x:
                return mid, iteration
            
            elif arr[mid] < x:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return -1, iteration


# generate a random 100 element list with random numbers 
arr = [i for i in range(100)]

# arr = [0, 2, 4, 8, 10, 12, 4, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
x = 22
print(binarySearch(arr, x))
