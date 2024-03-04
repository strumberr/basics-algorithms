
n = int(input())

steps = 0

while n > 0:

    digits = [int(digit) for digit in str(n)]
    max_digit = max(digits)
    n -= max_digit
    steps += 1
    
print(steps)