# شیفت
n, x = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 1
while cnt < x + 1:
    lst = lst[n-1:] + lst[: n-1]
    cnt += 1
    
print(*lst)