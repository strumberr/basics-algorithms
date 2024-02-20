import math

months = [2, 4, 7, 3, 8, 9, 1, 5, 4]

def findDuplicate(months):
    total_iterations = 0

    for i in range(len(months)):
        for j in range(i, len(months)):
            if months[i] > months[j]:
                months[i], months[j] = months[j], months[i]
            total_iterations += 1
        total_iterations += 1


    for el1, el2 in zip(months, months[1:]):
        if el1 == el2:
            return el1, total_iterations
        
        total_iterations += 1


