# آسمان شکر آباد
n, m = map(int, input().split())

lst = []
count = 0
for i in range(n):
    li = input()
    for ch in li:
        if ch == "*":
            count += 1

print(count)