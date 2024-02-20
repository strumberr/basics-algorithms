from eratosthenes import prime as primeSimple
from exercise1 import prime as primeEratosthenes

class Prime:
    def __init__(self, n):
        self.n = n

    def primeSimple(self):
        return primeSimple(self.n)

    def primeEratosthenes(self):
        return primeEratosthenes(self.n)

    def __str__(self):
        return f"Prime({self.n})"
    

if __name__ == "__main__":
    n = 7
    p = Prime(n)
    print