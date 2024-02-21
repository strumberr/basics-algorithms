import math
import random

def bubbleSort(content):

    n = len(content)

    total_iterations = 0

    for i in range(n):
        for j in range(0, n-i-1):

            total_iterations += 1

            if content[j] > content[j+1]:
                content[j], content[j+1] = content[j+1], content[j]


    return content, total_iterations

content = [3, 2, 5, 1, 0, 4]

print(bubbleSort(content))
