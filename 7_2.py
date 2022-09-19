# لیوان بازی
n, x = input().split()
n = int(n)

target = x
for _ in range(n):
    p2, p1 = input().split()
    if p1 == target:
        target = p2
    elif p2 == target:
        target = p1
           
print(target)