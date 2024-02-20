import math

openList = ["[","{","("]
closeList = ["]","}",")"]

string = "{[]{()}}"

def check(string):

    already_open = []

    for i in string:
        if i in openList:
            already_open.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(already_open) > 0) and (openList[pos] == already_open[len(already_open)-1])):
                already_open.pop()
            else:
                return "not good"
            
    if len(already_open) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    
print(check(string))

        