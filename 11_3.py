# رشته فیبوناچی

def fib(n, arr):
    if n == 1 :
        if arr[n] == 0:
            arr[n] = 1
        return arr[n]
    if n == 2:
        if arr[n] == 0:
            arr[n]= 2
        return arr[n]
    if arr[n] == 0:
        arr[n] = fib(n - 1, arr) + fib(n - 2, arr)
    return arr[n]

num = int(input())
arr = [0 for i in range(num + 1)]

fib(num, arr)
# print(arr)

for i in range(1, num+1):
    if i in arr:
        print('+', end="")
    if i not in arr:
        print("-", end="")
        