import math 


bookArray = [5, 7, 3, 4, 8, 2]

separator = 2

def check(mid, k):
    
        count = 0
    
        sum = 0
    
        for i in range(len(bookArray)):
    
            sum += bookArray[i]
    
            if sum > mid:
    
                count += 1
    
                sum = bookArray[i]
    
        return count <= k


def books(arr, k):

    l, r = max(arr), sum(arr)

    ans = None

    while l <= r:

        mid = l + (r - l) // 2

        if check(mid, k):
                
            ans = mid

            r = mid - 1

        else:
            l = mid + 1

    return ans

print(books(bookArray, separator))
            