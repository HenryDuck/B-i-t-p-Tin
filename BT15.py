a = int(input())

# Thi hành lệnh
if a <= 1:
    print(a, 'không phải là số nguyên tố')
elif a > 1:
    t = 0
    for i in range(1, a+1):
        if a % i == 0:
            t += 1
    if t == 2: print(a, 'là số nguyên tố')
    else: print(a, 'không phải là số nguyên tố')