m = int(input())
n = int(input())
sum = 0
for i in range(1, m+1):
    sum += int(i*(n*(n+1)/2))
print(sum)