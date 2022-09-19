# حرکت روی ظروف 
a, b, c  = list(map(int, input().split()))

if a == b and b == c:
    print(0)

elif a == b and b != c:
    print(2)
elif a!= b and b == c:
    print(2)
elif a == c and b != c:
    print(2)
elif a != b and b != c and a != c:
    if (a + b + c) / 3 == a or (a + b + c) / 3 == b or (a + b + c) / 3 == c:
        print(1)
    else:
        print(2)