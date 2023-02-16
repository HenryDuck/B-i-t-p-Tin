n = int(input('Có bao nhiêu số nguyên? '))

# Cách này nếu biết thì làm
# So = list(map(int, input('Nhập tất cả các số nguyên: ').split()))
# print(max(So))

Max = 0
for _ in range(n):
    b = int(input('Nhập số nguyên: '))
    if b > Max:
        Max = b
print(Max)