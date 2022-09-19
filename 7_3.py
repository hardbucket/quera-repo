# درگیر در
x, y = list(map(int, input().split()))
w, h = list(map(int, input().split()))

if w < x or h < y:
    print("yes")
else:
    print("no")