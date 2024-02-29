import math

arr = [6, 3, 5, 3, 3]

n = len(arr)

width = 1

def solve(arr, n):

    left_span = [0] * n

    for i in range(1, n):
        j = i - 1

        while j >= 0 and arr[j] <= arr[i]:
            left_span[i] += 1
            j -= 1

    # print(f"left_span: {left_span}")


    right_span = [0] * n

    for i in range(n-2, -1, -1):
        j = i + 1

        while j < n and arr[j] <= arr[i]:
            right_span[i] += 1
            j += 1

    # print(f"right_span: {right_span}")


    max_arm_length = 0
    
    for i in range(n):
        arm_length = min(left_span[i], right_span[i])
        max_arm_length = max(max_arm_length, arm_length)

    return max_arm_length

    
print(solve(arr, n))



