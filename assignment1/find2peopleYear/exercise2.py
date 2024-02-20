import math

months = [2, 4, 7, 3, 8, 9, 1, 5, 4]

def findDuplicate(months):

    res = 0

    total_iterations = 0

    for i in range(len(months)):
        for j in range(i, len(months)):
            if months[i] > months[j]:
                months[i], months[j] = months[j], months[i]

            total_iterations += 1

        res = months[i]
        
        if months[i] == months[i - 1]:

            return res, total_iterations


        total_iterations += 1

