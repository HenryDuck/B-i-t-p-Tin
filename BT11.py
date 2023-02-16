# ------------------------------------ #
#               Hướng dẫn
# Phần '#' là chữ hướng dẫn / đánh dấu
# ------------------------------------ #


# Kiểm tra số
while True:
    n = int(input())
    if n > 1:
        break
    print('Nhập lại số nguyên lớn hơn 1')
# Thực hiện lệnh
sum = 0
for a in range(2, n+1, 2):
    if a <= n:
        sum += a**2
print(sum)