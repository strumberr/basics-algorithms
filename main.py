from assignment1 import (findDuplicate1, 
                         findDuplicate2, 
                         findDuplicate3, 
                         primeSimple, 
                         primeEratosthenes)


from assignment2 import (Operations)


class OverallMain():
    
    def __init__(self, n, listNums):
        self.n = n
        self.list = listNums


    def findDuplicate(self):

        print(f"Repeated number using first method: {findDuplicate1(self.list)}, total iterations: {findDuplicate1(self.list)}")
        print(f"Repeated number using second method: {findDuplicate2(self.list)}, total iterations: {findDuplicate2(self.list)}")
        print(f"Repeated number using third method: {findDuplicate3(self.list)}, total iterations: {findDuplicate3(self.list)}")


    def prime(self):
        
        print(f"Prime number using first method primeSimple: {primeSimple(self.n)}, total iterations: {primeSimple(self.n)}")
        print(f"Prime number using second method Eratosthenes: {primeEratosthenes(self.n)}, total iterations: {primeEratosthenes(self.n)}")

    



# init class

overall_main = OverallMain(3, [2, 4, 7, 3, 8, 9, 1, 5, 4])
overall_main.findDuplicate()