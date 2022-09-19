# سراب
x, y = map(int, input().split())

if x % 2 == 0:
    if y == x:
        print(x + y)
    elif y == x - 2:
        print(x + y)
    else:
        print(-1)
if x % 2 != 0:
    if y == x:
        print(x + y - 1)
    elif y == x - 2:
        print(x + y - 1)
    else:
        print(-1)