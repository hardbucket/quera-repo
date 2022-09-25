# سامان‌بده!

n, k = list(map(int, input().split()))
names = [input() for name in range(n)]

result = {}
for name in names:
    result[name[:k]] = result.get(name[:k], 0) + 1

print(max(list(result.values())))