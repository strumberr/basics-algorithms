from exercise1 import findDuplicate as findDuplicate1
from exercise2 import findDuplicate as findDuplicate2
from exercise3 import findDuplicate as findDuplicate3


class Prime:
    def __init__(self, n):
        self.n = n

    def findDuplicate1(self):
        return findDuplicate1(self.n)
    
    def findDuplicate2(self):
        return findDuplicate2(self.n)
    
    def findDuplicate3(self):
        return findDuplicate3(self.n)


if __name__ == "__main__":

    n = [2, 4, 7, 3, 8, 9, 1, 5, 4]\
    
    p = Prime(n)
    
    print(f"Repeated number using first method: {p.findDuplicate1()[0]}, total iterations: {p.findDuplicate1()[1]}")
    print(f"Repeated number using second method: {p.findDuplicate2()[0]}, total iterations: {p.findDuplicate2()[1]}")
    print(f"Repeated number using third method: {p.findDuplicate3()[0]}, total iterations: {p.findDuplicate3()[1]}")