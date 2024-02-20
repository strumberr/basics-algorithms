import math

months = [2, 4, 7, 3, 8, 9, 1, 5, 4]

def findDuplicate(months):

    i = 0
    j = 1
    total_iterations = 0

    while i < len(months):

        if i != j and months[i] == months[j]:
            return months[i], total_iterations


        j += 1
        if j == len(months):
            i += 1
            j = i + 1

        total_iterations += 1

