from assignment1 import (findDuplicate1, 
                         findDuplicate2, 
                         findDuplicate3, 
                         primeSimple, 
                         primeEratosthenes)

# find duplicate argument type = list
# prime argument type = int

from assignment2 import (Operations, 
                         OperationsQueue, 
                         OperationsStack)

# Operations, OperationsQueue, OperationsStack argument type = list

from sorting import (bubbleSort, 
                     bogoSort, 
                     radixSort)

# bubbleSort, bogoSort, radixSort argument type = list


class OverallMain():
    
    def __init__(self, n, listNums):
        self.n = n
        self.list = listNums


    def findDuplicate(self):

        print(f"Repeated number using first method: {findDuplicate1(self.list)[0]}, total iterations: {findDuplicate1(self.list)[1]}")
        print(f"Repeated number using second method: {findDuplicate2(self.list)[0]}, total iterations: {findDuplicate2(self.list)[1]}")
        print(f"Repeated number using third method: {findDuplicate3(self.list)[0]}, total iterations: {findDuplicate3(self.list)[1]}")


    def prime(self):

        iterations = 0

        print(f"Prime number using first method primeSimple: {primeSimple(self.n, iterations)}, total iterations: {primeSimple(self.n, iterations)}")
        print(f"Prime number using second method Eratosthenes: {primeEratosthenes(self.n)}, total iterations: {primeEratosthenes(self.n)}")

    def sorting(self):

        print(f"Sorted list using bubbleSort: {bubbleSort(self.list)[0]}, total iterations: {bubbleSort(self.list)[1]}")
        print(f"Sorted list using bogoSort: {bogoSort(self.list)[0]}, total iterations: {bogoSort(self.list)[1]}")
        print(f"Sorted list using radixSort: {radixSort(self.list)[0]}, total iterations: {radixSort(self.list)[1]}")


# init class

overall_main = OverallMain(3, [2, 4, 7, 3, 8, 9, 1, 5, 4])
overall_main.findDuplicate()
overall_main.prime()
overall_main.sorting()