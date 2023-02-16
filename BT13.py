while True:
    n = int(input('Nhập số nguyên không âm: '))
    if n >= 0:
        break
    print('Vui lòng nhập lại số nguyên không âm')

sum = 1

if n != 0:
    for i in range(1, n+1):
        sum *= i
        
print(sum)
