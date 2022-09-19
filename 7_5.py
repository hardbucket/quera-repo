# توان دو
n = int(input())

for i in range(n//2):
    poly = 2 ** i
    if poly > n:
        print(poly)
        break