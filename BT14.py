n = int(input('Nhập số bị chia: '))
m = int(input('Nhập số chia: '))

# a là thương, b là dư
a = 0
b = 0

# Thi hành lệnh
while n > m:
    a += 1
    n -= m
b = m

print('Thương, dư:', a, b)