# دنباله‌ی ساده

def f(n):
    if n == 0 :
        return 5
    if n % 2 == 0:
        return f(n - 1) -21
    if n % 2 != 0:
        return f(n - 1) * f(n - 1)


n = int(input())

print(f(n))