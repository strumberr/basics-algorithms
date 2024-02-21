import math

class OperationsStack():

    def __init__(self, stack):
        self.stack = stack


    def is_empty(self):
        return not self.stack


    def push(self, item):
        # self.stack.append(item)
        self.stack = self.stack + [item]
        # print(self.stack)


    def pop(self):
        
        if not self.is_empty():

            return self.stack.pop()
        
        return None
    
    def notEnoughElements(self):
        if len(self.stack) < 2:
            print("not enough elements")
            return True
    
    def swp(self):
        if self.notEnoughElements(): return
        
        a = self.pop()
        b = self.pop()

        self.push(a)
        self.push(b)

        return self.stack


    def multiplyTopTwo(self):
        if self.notEnoughElements(): return
        
        a = self.pop()
        b = self.pop()

        # result = 0
        # for _ in range(b):
        #     result += a

        result = a * b

        self.push(b)
        self.push(a)

        return result, self.stack
    

    def addTopTwo(self):
        if self.notEnoughElements(): return
        
        a = self.pop()
        b = self.pop()

        result = a + b

        self.push(result)

        return result, self.stack
    

    def divideTopTwo(self):
        if self.notEnoughElements(): return
        
        a = self.pop()
        b = self.pop()

        result = a / b

        self.push(b)
        self.push(a)

        return result, self.stack
    
    def modulusTopTwo(self):
        if self.notEnoughElements(): return
        
        a = self.pop()
        b = self.pop()

        result = a % b

        self.push(b)
        self.push(a)

        return result, self.stack
    
    def duplicateTop(self):
        if self.notEnoughElements(): return
        
        a = self.pop()

        self.push(a)
        self.push(a)

        return a
    
    def powerElementTop(self, power):
        if self.notEnoughElements(): return
        
        # # duplicate the element x times to take the power, becuase we can't use the ** operator

        self.duplicateTop()
        
        for _ in range(power):
            self.multiplyTopTwo()

        return self.stack
    
            
        
    
    


operations_stack = OperationsStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(f"multiplyTopTwo: {operations_stack.multiplyTopTwo()[0]}, stack: {operations_stack.multiplyTopTwo()[1]}")
# print(f"swapped: {operations_stack.swp()}")
# print(f"addTopTwo sum: {operations_stack.addTopTwo()[0]}, stack: {operations_stack.addTopTwo()[1]}")
# print(f"divideTopTwo sum: {operations_stack.divideTopTwo()[0]}, stack: {operations_stack.divideTopTwo()[1]}")
# print(f"modulusTopTwo modulus: {operations_stack.modulusTopTwo()[0]}, stack: {operations_stack.modulusTopTwo()[1]}")
print(f"powerElementTop: {operations_stack.powerElementTop(3)}")