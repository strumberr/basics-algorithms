import math

# data structures
# without using any in built functions

class Operations():
    def __init__(self):
        pass

    def pop(self, listNums):
        return listNums[:-1]
    
    def popIndex(self, listNums, index):
        if index < 0 or index >= len(listNums):
            return "Index out of range"
        else:
            return listNums[:index] + listNums[index + 1:]
    
    def append(self, listNums, num):
        return listNums + [num]
    
    def insert(self, listNums, index, num):
        if index < 0 or index >= len(listNums):
            return "Index out of range"
        else:
            return listNums[:index] + [num] + listNums[index:]
    

    def add(self, listNums):
        return listNums[:-2] + [listNums[-1] + listNums[-2]]
    
    def sub(self, listNums):
        return listNums[:-2] + [listNums[-1] - listNums[-2]]
    

    def lengthArray(self, listNums):
        elements = 0

        for i in listNums:
            elements += 1

        return elements
    
    def accessElement(self, listNums, index):

        if index < 0 or index >= len(listNums):
            return "Index out of range"
        else:
            return listNums[index]
        
    
