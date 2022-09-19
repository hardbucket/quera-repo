# دایره عجیب
n, k = list(map(int, input().split()))

i = 1
count = 0
while True:
    i += k
    if n == 1:
        break
    if i > n:
        i -= n
    if i == 1:
        count += 1
        break
    count += 1
print(count)