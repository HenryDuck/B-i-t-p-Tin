while True:
    n = int(input('Nhập số nguyên dương: '))
    if n >= 1:
        break
    print('Vui lòng nhập lại số nguyên dương')

sum = 0
for i in range (1, n+1):
    sum += i*10 + 2
print(sum)