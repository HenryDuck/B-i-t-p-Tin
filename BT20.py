n = int(input('Nhập số n: '))

# Cách này hiểu thì làm
# a = list(map(int, input('Nhập tất cả các số nguyên đầu tiên: ').split()))
# sum = 0
# for i in a:
#    sum += i
# print(sum)

sum = 0
for i in range(1, n+1):
    a = int(input('Nhập số hạng thứ ' + str(i) +': '))
    sum += a
print(sum)