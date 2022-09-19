# کِوین و قدرت شالاپ
n = int(input())


if n % 2 == 0:
    sum = ((n / 2) * ((n / 2) + 1)) - (n / 2)
    size = n + 1
else:
    sum = (((n - 1)/ 2) * (((n - 1)/ 2) + 1))
    size = n + 1

ans = sum / size
print(f"{ans: 0.6f}")
