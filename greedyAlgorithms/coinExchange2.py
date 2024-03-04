
coins = [2, 5, 20]
x = 67

result = 0

for el in sorted(coins, reverse=True):
    while x >= el:
        print(x, el)
        x -= el
        result += 1
        
print(result)

print('------------------')

coins = [2, 5, 20]

x = 67

result = 0

for el in sorted(coins, reverse=True):
    result += x // el
    print(x, el)
    x %= el
    
print(result)
