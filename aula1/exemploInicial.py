n = 30
numDivisores = 0

for i in range(1, n + 1):
    if n % i == 0:  
        numDivisores += 1  

print(numDivisores)
