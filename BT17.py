n = int(input())

# Cái này không biết tại sao nó lại đúng
t = 0
while n >= 10:
    t += 1
    n //= 10
t += 1
print(t)